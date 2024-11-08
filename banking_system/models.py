from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings 

class Customer(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_number = models.PositiveIntegerField(validators=[MaxValueValidator(99999999999)]) 
    phone_number = models.CharField(max_length=15) 
    email = models.EmailField(max_length=100, unique=True)  
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['first_name', 'last_name','document_number','password'] 

    def __str__(self):
        return self.email

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=20)
    account_number = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    status = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.account_type} - {self.account_number}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]
    id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} for account {self.account.id}"
 