from meuapp.models.base import BaseModel
from django.db import models
from django.contrib.auth.models import User

class Account(BaseModel):
    owner = models.ManyToManyField(User, verbose_name= 'Account Owner')
    description = models.CharField(max_length=200, help_text='Description for your account')
    number = models.CharField(max_length=20, help_text='Insert your account number here.')
    balance = models.FloatField(default=0, help_text='Insert your initial balance.')
 
    class Meta:
        abstract = False

    def __str__(self):
        return f'{self.number}: {self.description} - {self.balance}'

    def update_balance(self, value):
        try:
            self.balance = self.balance + float(value)
            return True
        except:
            return False

    def get_balance(self):
        return self.balance

#aaa