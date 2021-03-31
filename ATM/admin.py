from django.contrib import admin
from .models.customer import Customer
from .models.transactions import Transactions


# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','lastname','account_no']


class AdminTransactions(admin.ModelAdmin):
    list_display = ['account_no','type','amount','balance']

admin.site.register(Customer,AdminCustomer)
admin.site.register(Transactions,AdminTransactions)