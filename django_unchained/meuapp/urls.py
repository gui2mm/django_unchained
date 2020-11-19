from django.urls import path
from . import views

app_name = 'meuapp'

urlpatterns = [
    path('article/', views.list, name="article_list"),
    path('article/create', views.create, name="article_create"),
    path('article/<int:article_id>', views.read, name="article_read"),
    path('article/delete/<int:article_id>', views.delete, name='article_delete'),
    path('article/update/<int:article_id>', views.update, name="article_update"),
]