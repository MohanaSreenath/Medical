from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('',include('Function.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('Function.urls')),
    path('hello/', include('Function.urls')),
    path('hello2/<str:name>/', include('Function.urls')),
    path('app/', include('Symp.urls')),
]
