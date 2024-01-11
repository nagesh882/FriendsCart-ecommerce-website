from django.urls import path
from store import views

urlpatterns = [
    path('', views.store, name='store' ),
    path('<slug:category_slug>', views.store, name='products_by_category' ),
]
