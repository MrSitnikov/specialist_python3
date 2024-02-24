from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('item/<int:id>/', views.out_item),
    path('items/', views.out_all_items),
]
