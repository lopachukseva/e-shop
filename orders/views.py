from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from common.views import TitleMixin
from orders.forms import OrderForm
from orders.models import Order
from products.models import Basket


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = "orders/success.html"
    title = "Успешно!"


class OrderCreateView(TitleMixin, CreateView):
    template_name = "orders/order-create.html"
    title = "Оформление заказа"
    form_class = OrderForm
    success_url = reverse_lazy("order_success")

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        order_id = self.object.id
        order = Order.objects.get(id=order_id)
        order.update_after_success()
        return HttpResponseRedirect(reverse("order_success"))

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)


class OrderListView(TitleMixin, ListView):
    title = "Заказы"
    template_name = "orders/orders.html"
    queryset = Order.objects.all()
    ordering = ("-id",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(initiator=self.request.user)


class OrderDetailView(DetailView):
    template_name = "orders/order.html"
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Заказ #{self.object.id}"
        return context
