from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ATM.models.customer import Customer

class Options(View):
    def post(self,request):
        pin = request.POST.get('pin')
        customer_id = request.session['customer']
        check_pin = Customer.get_customer_by_id(customer_id).pin
        print(type(pin),type(check_pin))
        if int(pin) == check_pin:
            return render(request,'options.html')

        else:
            error_message = "Incorrect Pin!!!"
            return render(request,'transactioncomplete.html',{'error':error_message})
