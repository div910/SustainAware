from django.urls import path, include
from sustainaware_backend.apps.marketplace import views

urlpatterns = [
    path('first/', views.first)
]