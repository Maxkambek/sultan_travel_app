from django.db import models
from accounts.models import Account
from main.models import Tour


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    order_amount = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    count_client = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone
