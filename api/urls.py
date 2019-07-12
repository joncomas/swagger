from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('ToDosView/<int:toDosItem_id>', views.ToDosView.as_view(), name='id-toDosItem'),
    path('ToDosView/', views.ToDosView.as_view(), name='all-Todos'),
]
