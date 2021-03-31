from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    account_no = models.IntegerField()
    current_balance = models.FloatField()
    pin = models.IntegerField()

    @staticmethod
    def get_customer_by_account_no(account_no):
        try:
            return Customer.objects.get(account_no=account_no)

        except:
            return False

    @staticmethod
    def get_customer_by_id(id):
        return Customer.objects.get(id=id)


    @staticmethod
    def withdraw(id,amount,balance):
        customer = Customer.objects.get(id=id)
        customer.current_balance = balance - amount
        customer.save()
            

