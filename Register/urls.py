from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name = 'register')
    #path('register/', views.register, name = 'register') #yo garda error aune raixa
]