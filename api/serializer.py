from dataclasses import fields
from rest_framework import serializers
from wallet.models import Customer, Wallet, Account, Card, Transaction, Loan, Receipt, Notifications


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email','age')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('User_id', 'balance')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_name', 'account_type', 'account_number')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('card_name', 'card_type', 'card_number')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_code','transaction_amount','transaction_number')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('loan_amount','loan_type','loan_number','loan_date')

class RecieptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('receipt_type','receipt_date','total_amount','receipt_file')

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('customer_id','customer_name','notification_status')


