from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path("api/products/", views.ProductListView.as_view(), name="store_home"),
    path("api/products/<str:id>/", views.Product.as_view(), name="store_home"),
]