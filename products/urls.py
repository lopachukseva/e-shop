from django.urls import path

from products import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.products, name="products"),
    path("products/category/<int:category_id>", views.products, name="category"),
    path("products/page/<int:page_number>", views.products, name="paginator"),
    path("basket/add/<int:product_id>", views.basket_add, name="basket_add"),
    path("basket/remove/<int:basket_id>", views.basket_remove, name="basket_remove"),
]
