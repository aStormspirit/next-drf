from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path("api/products/", views.ProductListView.as_view(), name="store_home"),
    path("api/products/<str:id>/", views.Product.as_view(), name="product"),
    path("api/order", views.CreateOrder.as_view(), name="create_order"),
    path("api/orders", views.OrdersList.as_view(), name="list_order"),
    path("api/csrf", views.get_csrf, name="csrf_token"),
]
