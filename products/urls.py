from django.urls import path

from products import views

# from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("products/", views.ProductsListView.as_view(), name="products"),
    # path("products/", cache_page(30)(views.ProductsListView.as_view()), name="products"),
    path("products/category/<int:category_id>", views.ProductsListView.as_view(), name="category"),
    path("products/page/<int:page>", views.ProductsListView.as_view(), name="paginator"),
    path("basket/add/<int:product_id>", views.basket_add, name="basket_add"),
    path("basket/remove/<int:basket_id>", views.basket_remove, name="basket_remove"),
]
