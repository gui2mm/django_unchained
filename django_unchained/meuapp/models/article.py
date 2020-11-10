from meuapp.models.base import BaseModel
from django.db import models
from meuapp.models.reporter import Reporter
from meuapp.models.magazine import Magazine

class Article(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Article title', help_text='Insert the article title')
    pub_date = models.DateTimeField(verbose_name='Publication date', help_text='Insert the publication date time')
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    magazines = models.ManyToManyField(Magazine, verbose_name='Magazines', help_text='Select magazines')

    class Meta:
        abstract = False

    def __str__(self):
        return self.title

    #aaa