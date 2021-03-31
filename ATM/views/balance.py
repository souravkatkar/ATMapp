from django.shortcuts import render
from django.views import View
from django.http import HttpResponse




class Balance(View):
    
    def get(self,request):
        return render(request,'balance.html')