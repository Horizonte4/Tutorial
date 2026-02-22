from django.urls import path
from .views import HomeView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductIndexView.as_view(), name="product.index"),
    path("products/create", ProductCreateView.as_view(), name="product.create"),
    path("products/created", ProductCreatedView.as_view(), name="product-created"),
    path("products/<int:id>", ProductShowView.as_view(), name="product.show"),
]