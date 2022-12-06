from django.urls import path, include
from bilhete import views

urlpatterns = [
    path('', views.rifa, name='Rifa'),
    path('gerar', views.gerarNumero, name='Gerar'),
]