from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ATM.models.customer import Customer


class Showbalance(View):
    def get(self,request):
        customer_id = request.session['customer']
        balance = Customer.get_customer_by_id(customer_id).current_balance
        return render(request,'showbalance.html',{'balance':balance})