from django.shortcuts import render
from django.views import View
from django.http import HttpResponse



class Currentwithdrawl(View):
    def get(self,request):
        return render(request,'cashwithdrawl.html')