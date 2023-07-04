from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"products", views.ProductModelViewSet)
router.register(r"basket", views.BasketModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("product-categories/", views.ProductCategoryListAPIView.as_view(), name="product_categories"),
]
