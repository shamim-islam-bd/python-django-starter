from django.db import models

# Create your models here.
class pay_method(models.Model):
    pay_id = models.IntegerField()
    pay_option = models.CharField(max_length=50)
    min_pay = models.IntegerField()
