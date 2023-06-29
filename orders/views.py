from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from common.views import TitleMixin
from orders.forms import OrderForm


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = "orders/success.html"
    title = "Успешно!"


class OrderCreateView(TitleMixin, CreateView):
    template_name = "orders/order-create.html"
    title = "Оформление заказа"
    form_class = OrderForm
    success_url = reverse_lazy("order_success")

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)
