from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ATM.models.customer import Customer





class Pin(View):
    def post(self,request):
        account_no = request.POST.get('account_no')
        customer = Customer.get_customer_by_account_no(account_no)
        if customer:
            request.session['customer'] = customer.id
            print(request.session['customer'])
            fullname = customer.name + ' ' + customer.lastname
            return render(request,'pin.html',{'customer':fullname})

        else:
            error_message = "Invalid Account Number"
            return render(request,'home.html',{'error':error_message})

    
