from rest_framework import serializers
from .models import Customer, Account, Transaction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'document_number', 'phone_number', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        customer = Customer(**validated_data)
        customer.set_password(validated_data['password'])  
        customer.save()
        return customer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_type', 'account_number', 'status', 'balance', 'customer']

class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("The deposit value must be positive.")
        return value

    def update(self, instance, validated_data):
        amount = validated_data.get('amount')
        instance.balance += amount
        instance.save()
        return instance
    
class WithdrawalSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("The deposit value must be positive.")
        
        return value

    def update(self, instance, validated_data):
        amount = validated_data.get('amount')

        if instance.balance < amount:
            raise serializers.ValidationError("You don't have this value in your account")
        else:
            instance.balance -= amount
            instance.save()

        return instance 

    