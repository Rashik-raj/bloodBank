from django.shortcuts import render
from Register.models import Donors
# Create your views here.
def index(request):
    return render(request, 'home.htm')

def search(request):
    district = request.POST['district']
    bloodGroup = request.POST['bloodGroup']
    datas = Donors.objects.all()
    results = []
    for data in datas:
        if (data.district == district and data.bloodGroup == bloodGroup):
            results.append(data)
    return render(request, 'searchResult.htm', { 'results' : results })