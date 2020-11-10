from meuapp.models.base import BaseModel
from django.db import models

class Reporter(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Full Name', help_text='Insert the full name')
    email = models.EmailField(verbose_name='Email', help_text='Insert the professional email')
    cpf = models.CharField(max_length=11, verbose_name='Insert the CPF Number', help_text='Insert your CPF number')

    class Meta:
        abstract = False
    
    def __str__(self):
        return self.name
    #aaa