from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('store/', views.store, name='store'), 
    path('about/', views.about, name='about'),
    
]