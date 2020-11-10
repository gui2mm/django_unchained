from meuapp.models.base import BaseModel
from django.db import models

class Magazine(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Magazine name', help_text='Insert the magazine name')
    edition = models.IntegerField(verbose_name='Magazine edition number', help_text='Insert the magazine number')
    
    class Meta:
        abstract = False
    
    def __str__(self):
        return f'{self.name}: {self.edition}'
    
    #aaa