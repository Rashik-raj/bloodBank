from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('home/', include('Home.urls')),
    path('register/', include('Register.urls')),
    path('bloodRequest/', include('BloodRequest.urls'))
]
