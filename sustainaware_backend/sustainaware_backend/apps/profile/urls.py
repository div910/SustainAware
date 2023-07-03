from django.urls import path, include
from sustainaware_backend.apps.profile import views

urlpatterns = [
    path('login/', views.login),
    path('first/', views.first)
]