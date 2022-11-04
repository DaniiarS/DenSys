from django.contrib import admin
from django.urls import path, include
from .views import ItemsView,ItemView

urlpatterns = [
    path('items/', ItemsView, name='items'),
    path('item/<int:nm>/', ItemView, name='item'),
]
