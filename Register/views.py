from django.shortcuts import render
from .models import Donors
# Create your views here.
def register(request):
    return render(request, 'register.htm')

def registerUser(request):
    x = Donors()
    x.firstName = request.POST['firstName']
    x.middleName = request.POST['middleName']
    x.lastName = request.POST['lastName']
    x.district = request.POST['district']
    x.address = request.POST['address']
    x.primaryContact = request.POST['primaryContact']
    x.secondaryContact = request.POST['secondaryContact']
    x.email = request.POST['email']
    x.bloodGroup = request.POST['bloodGroup']
    x.gender = request.POST['gender']
    x.save()
    return render(request, 'home.htm')