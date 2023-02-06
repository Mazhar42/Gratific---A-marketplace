from django.urls import path
from .views import detail, add_new_item,delete_item

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', detail, name="detail"),
    path('<int:pk>/delete/', delete_item, name="delete"),
    path('new/', add_new_item, name="newitem"),
]