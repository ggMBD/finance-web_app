#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.CharField(max_length = 200, verbose_name = "item")
    amount = models.DecimalField(max_digits=8,decimal_places=2, verbose_name = "amount")
    date = models.DateField(verbose_name = "Data")

    def __unicode__(self):
        return self.item
