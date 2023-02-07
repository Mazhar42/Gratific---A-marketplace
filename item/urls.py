from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.search, name="search"),
    path('new/', views.add_new_item, name="newitem"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete_item, name="delete"),
    path('<int:pk>/edit/', views.edit_item, name="edit"),
]