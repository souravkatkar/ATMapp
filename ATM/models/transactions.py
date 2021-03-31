from django.db import models

class Transactions(models.Model):
    time = models.CharField(max_length=50,null=True)
    account_no = models.IntegerField()
    balance = models.FloatField()
    amount = models.FloatField()
    type = models.IntegerField()

    def register(self):
        self.save()

    @staticmethod
    def get_transactions_by_account_no(account_no):
        return Transactions.objects.filter(account_no = account_no).order_by('-time')