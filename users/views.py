from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


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


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = "users/email_verification.html"
    title = "Подтвердение учетной записи"

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        code = kwargs.get("code")
        email = kwargs.get("email")
        user = User.objects.get(email=email)
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return context
        return HttpResponseRedirect(reverse("index"))

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
