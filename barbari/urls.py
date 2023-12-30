from .views import combined_list
from django.urls import path

urlpatterns = [
    path('', combined_list, name='combined_list'),
]
