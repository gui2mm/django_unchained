from meuapp.models.base import BaseModel
from meuapp.models.person import Person
from django.db import models

class Passport(BaseModel):
    number = models.CharField(max_length=10, verbose_name='Passport Number', help_text='Insert your passport number')
    issue_date = models.DateField(verbose_name='Issue Date', help_text='Insert the issue date of the passport.')
    expiration_date = models.DateField(verbose_name='Expiration Date', help_text='Insert the expiration date')
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        abstract = False

    def issue_passport(self, issue_date, expiration_date):
        pass
#aaa