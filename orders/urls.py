from django.urls import path
from orders import views

urlpatterns = [
    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path("success/", views.SuccessTemplateView.as_view(), name="order_success"),
    path("", views.OrderListView.as_view(), name="orders_list"),
    path("order/<int:pk>/", views.OrderDetailView.as_view(), name="order"),
]
