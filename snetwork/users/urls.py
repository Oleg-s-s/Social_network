from django.urls import include, path
from .views import dashboardU, register

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", dashboardU),
    path("register/", register, name="register"),
]