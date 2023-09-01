from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_Bage, name="Home"),
    path('boards/<int:board_id>/', views.board_topics, name="board_topics"),
    path('boards/<int:board_id>/new/', views.new_topic, name="new_topic"),
]