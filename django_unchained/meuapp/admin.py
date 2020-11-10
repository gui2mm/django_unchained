from django.contrib import admin
from meuapp.models.account import Account
from meuapp.models.person import Person
from meuapp.models.passport import Passport
from meuapp.models.reporter import Reporter
from meuapp.models.magazine import Magazine
from meuapp.models.article import Article

# Register your models here.


admin.site.register(Account)
admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Reporter)
admin.site.register(Magazine)
admin.site.register(Article)