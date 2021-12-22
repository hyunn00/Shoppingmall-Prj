from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/', views.board_list, name = 'board_list'),
    path('write/', views.board_write, name = 'board_write'),
    path('detail/<int:pk>/', views.board_detail),
]