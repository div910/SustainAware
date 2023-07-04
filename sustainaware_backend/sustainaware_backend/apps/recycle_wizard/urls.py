from django.urls import path, include
from sustainaware_backend.apps.recycle_wizard import views

urlpatterns = [
    path('add_post', views.add_post),
    path('get_post', views.get_post),
    path('first/', views.first)
]