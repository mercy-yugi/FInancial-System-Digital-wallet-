from django.shortcuts import render
from wallet.models import *
from . import serializer
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=serializer.CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=serializer.WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):
        queryset=Account.objects.all()
        serializer_class=serializer.AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=serializer.CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=serializer.TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=serializer.LoanSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
        queryset=Receipt.objects.all()
        serializer_class=serializer.RecieptSerializer

class NotificationsViewSet(viewsets.ModelViewSet):
        queryset=Notifications.objects.all()
        serializer_class=serializer.NotificationsSerializer

# Account Deposit
class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)

# Account Transfer
class AccountTransferView(views.APIView):
   """
   This class allows transfer of funds from one account to another account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.transfer(amount)
       return Response(message, status=status)

# Account Withdrawal
class AccountWithdrawView(views.APIView):
   """
   This class allows withdrawal of funds from an account.
   Accepts this JSON data
   {
       "account_id": 12,
       "amount": 500
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.withdraw(amount)
       return Response(message, status=status)

# Account Request Loan
class AccountRequestLoanView(views.APIView):
   """
   This class allows loan request from an account.
   Accepts this JSON data
   {
       "account_id": 12,
       "amount": 500
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.requestLoan(amount)
       return Response(message, status=status)

# Account Loan Repayment
class AccountRepayLoanView(views.APIView):
   """
   This class allows loan repayment to an account.
   Accepts this JSON data
   {
       "account_id": 12,
       "loan_amount": 1000
       "amount": 500
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.repay_loan(amount)
       return Response(message, status=status)

# Account Buy Airtime
class AccountBuyAirtimeView(views.APIView):
   """
   This class allows purchase of airtime from an account.
   Accepts this JSON data
   {
       "account_id": 12,
       "amount": 500
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.buy_airtime(amount)
       return Response(message, status=status)
