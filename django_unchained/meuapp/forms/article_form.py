from django import forms
from django.forms import TextInput
from meuapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args,**kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs['class'] = 'form-control'