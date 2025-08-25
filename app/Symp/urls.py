from django.urls import path
from . import views
urlpatterns = [
    path('input/',views.run, name="run"),
    path('run/', views.run, name="run"),
    path('opt/',views.run_opt, name='run_opt'),
    path('results/',views.run_opt, name='run_opt'),
    path('details/',views.re_run, name='re_run'),
]