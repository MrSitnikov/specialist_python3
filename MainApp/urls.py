from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('item/<int:item_id>/', views.get_item, name='item_detail'),
    path('items/', views.out_all_items, name='items'),
]
