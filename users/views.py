from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from users.models import User


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    success_message = "Поздравляем! Вы успешно прошли регистрацию!"
    title = "Регистрация"


class UserLoginView(TitleMixin, LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    title = "Авторизация"


class UserProfileView(TitleMixin, UpdateView):
    model = User
    template_name = "users/profile.html"
    form_class = UserProfileForm
    title = "Профиль"

    def get_success_url(self):
        return reverse_lazy("profile", args={self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["basket"] = Basket.objects.filter(user=self.request.user)
        return context

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse("index"))

# def login(request):
#     if request.method == "POST":
#         login_form = UserLoginForm(data=request.POST)
#         if login_form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(redirect_to=reverse("index"))
#     else:
#         login_form = UserLoginForm()
#
#     context = {"login_form": login_form}
#     return render(request, "users/login.html", context)

# @login_required
# def profile(request):
#     if request.method == "POST":
#         profile_form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if profile_form.is_valid():
#             profile_form.save()
#             return HttpResponseRedirect(redirect_to=reverse("profile"))
#     else:
#         profile_form = UserProfileForm(instance=request.user)
#
#     basket = Basket.objects.filter(user=request.user)
#
#     context = {
#         "title": "Profile",
#         "profile_form": profile_form,
#         "basket": basket,
#     }
#     return render(request, "users/profile.html", context)


# def register(request):
#     if request.method == "POST":
#         register_form = UserRegistrationForm(data=request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request, "Поздравляем! Вы успешно прошли регистрацию!")
#             return HttpResponseRedirect(reverse("login"))
#     else:
#         register_form = UserRegistrationForm()
#
#     context = {"register_form": register_form}
#     return render(request, "users/register.html", context)
