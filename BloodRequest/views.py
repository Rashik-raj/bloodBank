from django.shortcuts import render

# Create your views here.
def bloodRequest(request):
    return render(request, 'bloodRequest.htm')