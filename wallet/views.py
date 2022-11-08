from ast import If
from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def register_customer(request):  #1
    from .forms import CustomerRegistrationForm
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})

def list_customers(request):
    customers = forms.Customer.objects.all()
    return render(request,"wallet/list_customers.html",{"customers":customers})


def wallet_information(request):   #2
    if request.method == 'POST':
        form = forms.WalletInformation()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.WalletInformation()
    return render(request,"wallet/wallet_information.html",{"form":form})

def list_wallet_information(request):
    wallets = forms.Wallet.objects.all()
    return render(request,"wallet/list_wallet_information.html",{"wallets":wallets})


def account_details(request):   #3
    if request.method == 'POST':
        form = forms.AccountDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.AccountDetails()
    return render(request,"wallet/account_details.html",{"form":form})

def list_accounts(request):
    accounts = forms.Account.objects.all()
    return render(request,"wallet/list_accounts.html",{"accounts":accounts})


def transaction_details(request):  #4
    if request.method == 'POST':
        form = forms.TransactionDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.TransactionDetails()
    return render(request,"wallet/transaction_details.html",{"form":form})

def list_transactions(request):
    transactions = forms.Transaction.objects.all()
    return render(request,"wallet/list_transactions.html",{"transactions":transactions})


def card_details(request):  #5
    if request.method == 'POST':
        form = forms.CustomerCardDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.CustomerCardDetails()
    return render(request,"wallet/card_details.html",{"form":form})

def list_cards(request):
    cards = forms.Card.objects.all()
    return render(request,"wallet/list_cards.html",{"cards":cards})


def third_party_details(request):   #6
    if request.method == "POST":
        form = forms.ThirdPartyDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.ThirdPartyDetails()
    return render(request,"wallet/third_party_details.html",{"form":form})

def list_third_party(request): 
    third_parties = forms.ThirdParty.objects.all()
    return render(request,"wallet/list_third_party.html",{"third_parties":third_parties})

def notify_customer(request):  #7
    if request.method == "POST":
        form = forms.CustomerNotifications()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.CustomerNotifications()
    return render(request,"wallet/notify_customer.html",{"form":form})

def list_notifications(request):
    notification = forms.Notifications.objects.all()
    return render(request,"wallet/list_notifications.html",{"notifications":notification})

def recieve_reciept(request):   #8
    if request.method == "POST":
        form = forms.TransactionReciept()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.TransactionReciept()
    return render(request,"wallet/recieve_reciept.html",{"form":form})

def list_reciepts(request):
    reciepts = forms.Receipt.objects.all()
    return render(request,"wallet/list_reciepts.html",{"reciepts":reciepts})



def loan_details(request):  #9
    if request.method == "POST":
        form = forms.LoanDetails()
        if form.is_valid():
            user = form.save()
    else:
        form = forms.LoanDetails()
    return render(request,"wallet/loan_details.html",{"form":form})

def list_loans(request):
    loans = forms.Loan.objects.all()
    return render(request,"wallet/list_loans.html",{"loans":loans})


def customer_reward(request):   #10
    if request.method == "POST":
        form = forms.CustomerReward()
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerReward()
    return render(request,"wallet/customer_reward.html",{"form":form})

def list_reward(request):
    rewards = forms.Reward.objects.all()
    return render(request,"wallet/list_reward.html",{"rewards":rewards})


def customer_profile(request, id):
    customers = models.Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customers":customers})


def edit_customer_profile(request, id):
    customer = models.Customer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile",  id=customer.id)
    else:
        form = forms.CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_customer_profile.html",{"form":form})



def account_profile(request, id):
    accounts = models.Account.objects.get(id=id)
    return render(request,"wallet/account_profile.html",{"accounts":accounts})

def edit_wallet_accounts(request,id):
    account= models.Account.objects.get(id=id)
    if request.method == 'POST':
        form = forms.AccountDetails(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile",  id=account.id)
    else:
        form = forms.AccountDetails(instance=account)
        return render(request, "wallet/edit_wallet_accounts.html",{"form":form})


def wallet_details(request, id):
    wallets = models.Wallet.objects.get(id=id)
    return render(request, "wallet/wallet_details.html", {"wallets":wallets})

def edit_wallet_details(request, id):
    wallet = models.Wallet.objects.get(id=id)
    if request.method == "POST":
        form = forms.WalletInformation(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_details", id=wallet.id)
    else:
        form = forms.WalletInformation(instance=wallet)
        return render(request, "wallet/edit_wallet_details.html", {"form": form})

def card_display(request, id):
    cards = models.Card.objects.get(id=id)
    return render(request, "wallet/card_display.html", {"cards": cards})

def edit_card(request, id):
    card = models.Card.objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerCardDetails(request.POST,instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_display",  id=card.id)
    else:
        form = forms.CustomerCardDetails(instance=card)
        return render(request,"wallet/edit_card.html",{"form":form})
        

def transaction_display(request,id):
    transactions = models.Transaction.objects.get(id=id)
    return render(request,"wallet/transaction_display.html",{"transactions":transactions})

def edit_transaction(request,id):
    transaction = models.Transaction.objects.get(id=id)
    if request.method == "POST":
        form = forms.TransactionDetails(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_display",  id=transaction.id)
    else:
        form = forms.TransactionDetails(instance=transaction)
        return render(request,"wallet/edit_transaction.html",{"form":form})


def reciept_display(request,id):
    reciepts = models.Receipt.objects.get(id=id)
    return render(request,"wallet/reciept_display.html",{"reciepts":reciepts})

def edit_reciept(request,id):
    reciept = models.Receipt.objects.get(id=id)
    if request.method == "POST":
        form = forms.TransactionReciept(request.POST,instance=reciept)
        if form.is_valid():
            form.save()
            return redirect("receipt_display",  id=reciept.id)

    else:
        form = forms.TransactionReciept(instance=reciept)
        return render(request,"wallet/edit_reciept.html",{"form":form})


        
