from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


def register(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Поздравляем! Вы успешно прошли регистрацию!")
            return HttpResponseRedirect(reverse("login"))
    else:
        register_form = UserRegistrationForm()

    context = {"register_form": register_form}
    return render(request, "users/register.html", context)


def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_to=reverse("index"))
    else:
        login_form = UserLoginForm()

    context = {"login_form": login_form}
    return render(request, "users/login.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        profile_form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(redirect_to=reverse("profile"))
    else:
        profile_form = UserProfileForm(instance=request.user)

    basket = Basket.objects.filter(user=request.user)

    context = {
        "title": "Profile",
        "profile_form": profile_form,
        "basket": basket,
    }
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))
