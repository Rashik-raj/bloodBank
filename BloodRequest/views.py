from django.shortcuts import render
from .models import requests
# Create your views here.
def bloodRequest(request):
    return render(request, 'bloodRequest.htm')

def requestBlood(request):
    x = requests()
    x.name = request.POST['fullName']
    x.district = request.POST['district']
    x.address = request.POST['address']
    x.primaryContact = request.POST['primaryContact']
    x.secondaryContact = request.POST['secondaryContact']
    x.email = request.POST['email']
    x.bloodGroup = request.POST['bloodGroup']
    x.description = request.POST['description']
    x.save()
    return render(request, 'home.htm')