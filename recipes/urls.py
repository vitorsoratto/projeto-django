from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index),
    path('recipes/<int:id>/', views.recipe),
]
