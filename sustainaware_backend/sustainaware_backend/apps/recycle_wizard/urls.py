from django.urls import path, include
from sustainaware_backend.apps.recycle_wizard import views

urlpatterns = [
    path('first/', views.first)
]