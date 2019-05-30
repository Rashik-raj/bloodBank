from django.urls import path
from . import views
urlpatterns = [
    path('', views.bloodRequest, name = 'bloodRequest'),
    path('requestBlood/', views.requestBlood, name = 'requestBlood')
]
