from django.urls import path
from users import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", login_required(views.UserProfileView.as_view()), name="profile"),
]
