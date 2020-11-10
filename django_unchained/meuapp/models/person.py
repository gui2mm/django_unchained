from meuapp.models.base import BaseModel
from django.db import models

class Person(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Full Name', help_text='Insert your name')
    birth_date = models.DateField(verbose_name='Birth Date', help_text='Insert your birth date')
    cpf = models.CharField(max_length=11, verbose_name='CPF Number', help_text='Insert your CPF number')
    
    class Meta:
        abstract = False

    def check_visa(self, place, date):
        #TODO: Implementar metodo para verificação do visto
        pass
    
    def __str__(self):
        return self.name

#aaa