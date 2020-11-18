from django.urls import path
from .views import product_list, product_detail
# from .views import ProductDetailView, ProductListView


urlpatterns = [
    # path("", ProductListView.as_view(), name="product-list"),
    # path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail")
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail")
]
