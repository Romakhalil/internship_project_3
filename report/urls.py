from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_work, name='submit_work'),
    # Define other URL patterns for the report app here
]
