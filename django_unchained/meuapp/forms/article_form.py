from django import forms
from meuapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        field = ['title', 'reporter', 'magazines']