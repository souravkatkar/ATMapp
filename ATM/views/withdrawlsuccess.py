from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ATM.models.customer import Customer
from ATM.models.transactions import Transactions
from datetime import datetime

class Withdrawlsuccess(View):
    def post(self,request):
        amount = float(request.POST.get('amount'))
        
        customer_id = request.session['customer']
        customer = Customer.get_customer_by_id(customer_id)
        balance = customer.current_balance
        print(type(balance),type(amount))
        if balance >= amount:
            time = datetime.now()
            dt_string = time.strftime("%d/%m/%Y %H:%M:%S")
            print(dt_string)
            Customer.withdraw(customer_id,amount,balance)
            transaction = Transactions(amount=amount,balance = balance - amount,account_no = customer.account_no,type=0,time = dt_string)
            transaction.register()
            return render(request,'withdrawlsuccess.html')

        else:
            error_message = "You don't have sufficient balance"
            return render(request,'transactioncomplete.html',{'error':error_message})
