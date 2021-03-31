"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.index import Index
from .views.pin import Pin
from .views.options import Options
from .views.withdrawl import Withdrawl
from .views.balance import Balance
from .views.currentwithdrawl import Currentwithdrawl
from .views.savingswithdrawl import Savingswithdrawl
from .views.withdrawlsuccess import Withdrawlsuccess
from .views.transactioncomplete import Transactioncomplete
from .views.showbalance import Showbalance
from .views.ministatement import Ministatement

urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('pin',Pin.as_view(),name='pin'),
    path('options',Options.as_view(),name='options'),
    path('withdrawl',Withdrawl.as_view(),name='withdrawl'),
    path('balance',Balance.as_view(),name='balance'),
    path('savingswithdrawl',Savingswithdrawl.as_view(),name='savingswithdrawl'),
    path('currentwithdrawl',Currentwithdrawl.as_view(),name='currentwithdrawl'),
    path('withdrawlsuccess',Withdrawlsuccess.as_view(),name='withdrawlsuccess'),
    path('showbalance',Showbalance.as_view(),name='showbalance'),
    path('transactioncomplete',Transactioncomplete.as_view(),name='transactioncomplete'),
    path('ministatement',Ministatement.as_view(),name = 'ministatement'),
    
    

]
