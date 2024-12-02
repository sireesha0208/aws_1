from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.trip_request_view, name='trip_dashboard'),
    
]
