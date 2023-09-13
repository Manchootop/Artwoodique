from django.urls import path
from django.views.generic import ListView

from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('catalog/<int:pk>/', views.ProductDetailsView.as_view(), name='catalog-details'),
    path('shop/', views.CollectionView.as_view(), name='shop'),
    path('faq/', views.FAQView.as_view(), name='faq'),
]