from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name', 'last_name',)
admin.site.register(Customer, CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('User_id','balance','status','time',)
    search_fields = ('status','User_id',)
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name','account_type','account_number','wallet',)
    search_fields = ('account_number','account_name',)
admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_code','transaction_type','transaction_time','transaction_fee',)
    search_fields = ('transaction_code','transaction_time',)
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name','card_type','card_issuer','cvv_code','date_issued',)
    search_fields = ('card_issuer','card_name',)
admin.site.register(Card, CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ('party_name','party_id','account','phone_number',)
    search_fields = ('party_name','party_id',)
admin.site.register(ThirdParty, ThirdPartyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('customer_name','notification_date_time','notification_status','recipient',)
    search_fields = ('customer_name','notification_date_time',)
admin.site.register(Notifications, NotificationsAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_type','receipt_date','account_number','receipt_file','total_amount',)
    search_fields = ('receipt_type','receipt_date',)
admin.site.register(Receipt, ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_type','loan_amount','loan_date','interest_rate','loan_due_date',)
    search_fields = ('loan_type','loan_amount',)
admin.site.register(Loan, LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('reward_date','customer_id','reward_points','transaction',)
    search_fields = ('reward_date','reward_points',)
admin.site.register(Reward, RewardAdmin)