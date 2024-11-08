
from rest_framework import status
from .models import Account, Transaction

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AccountSerializer, CustomerSerializer, DepositSerializer, WithdrawalSerializer

class CustomerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        validation = CustomerSerializer(data=request.data)
        if validation.is_valid():
            validation.save()
            return Response("User created successfully", status=status.HTTP_201_CREATED)
        return Response(validation.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AccountCreateView(APIView):
    def post(self, request):
        validation = AccountSerializer(data=request.data)
        if validation.is_valid():
            validation.save()
            return Response("Account created successfully", status=status.HTTP_201_CREATED)
        return Response(validation.errors, status=status.HTTP_400_BAD_REQUEST)

class DepositView(APIView):
     def post(self, request, account_id):
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(account, serializer.validated_data)
            Transaction.objects.create(
                transaction_type='deposit',
                amount=serializer.validated_data['amount'],
                account=account
            )

            return Response({
                "message": "Deposit successful",
                "new_balance": account.balance
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WithdrawalView(APIView):
     def post(self, request, account_id):
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WithdrawalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(account, serializer.validated_data)
            Transaction.objects.create(
                transaction_type='withdrawal',
                amount=serializer.validated_data['amount'],
                account=account
            )

            return Response({
                "message": "withdrawal successful",
                "new_balance": account.balance
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class BalanceView(APIView):
    def get(self, request, account_id, *args, **kwargs):
        try:
            account = Account.objects.get(id=account_id)
            return Response({
            "Your curently balance": account.balance
        }, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({"error":"Account not found"}, status=status.HTTP_404_NOT_FOUND)
        
        