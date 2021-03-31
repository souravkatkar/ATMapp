from django.shortcuts import render
from django.views import View
from django.http import HttpResponse



class Withdrawl(View):
    def get(self,request):
        return render(request,'withdrawl.html')