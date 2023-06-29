from django.urls import path
from orders import views

urlpatterns = [
    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path("success/", views.SuccessTemplateView.as_view(), name="order_success"),
]
