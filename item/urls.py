from django.urls import path
from .views import detail, add_new_item

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', detail, name="detail"),
    path('new/', add_new_item, name="newitem"),
]