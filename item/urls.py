from django.urls import path
from .views import detail, add_new_item,delete_item,edit_item,search

app_name = 'item'

urlpatterns = [
    path('', search, name="search"),
    path('<int:pk>/', detail, name="detail"),
    path('<int:pk>/delete/', delete_item, name="delete"),
    path('<int:pk>/edit/', edit_item, name="edit"),
    path('new/', add_new_item, name="newitem"),
]