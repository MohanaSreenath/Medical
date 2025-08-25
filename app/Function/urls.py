from django.urls import path
from Function import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('hello/<str:name>/', views.hello2, name="hello2"),
]