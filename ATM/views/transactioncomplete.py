from django.shortcuts import render
from django.views import View
from django.http import HttpResponse




class Transactioncomplete(View):
    def get(self,request):
        request.session.clear()
        return render(request,'transactioncomplete.html')