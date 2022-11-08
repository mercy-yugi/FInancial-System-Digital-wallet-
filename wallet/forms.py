from dataclasses import fields
from pyexpat import model
from django import forms 
from .models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet
class CustomerRegistrationForm(forms.ModelForm):
    class Meta: 
        model = Customer
        fields = "__all__"

class WalletInformation(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"

class AccountDetails(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class TransactionDetails(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"

class CustomerCardDetails(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"

class ThirdPartyDetails(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields = "__all__"

class CustomerNotifications(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"

class TransactionReciept(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"

class LoanDetails(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"

class CustomerReward(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"