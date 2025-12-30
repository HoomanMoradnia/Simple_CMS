from django.urls import path
from . import views

app_name = 'weblog'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<slug:slug>', views.article_detail, name='article_detail'),
]