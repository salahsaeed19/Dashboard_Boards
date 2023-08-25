from django.urls import path
from . import views

urlpatterns = [
    path('', views.Show_Text, name="Show_Text"),
]