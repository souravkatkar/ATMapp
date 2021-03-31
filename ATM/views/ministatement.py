from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ATM.models.customer import Customer
from ATM.models.transactions import Transactions


class Ministatement(View):
    def get(self,request):

        customer_id = request.session['customer']
        customer= Customer.get_customer_by_id(customer_id)
        transactions = Transactions.get_transactions_by_account_no(customer.account_no)
        
    
        return render(request,'ministatement.html',{'transactions':transactions})