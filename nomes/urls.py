from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerar_nome, name='gerar_nome'),
]
