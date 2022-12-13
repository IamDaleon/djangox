from django.urls import path

from .views import HomePageView, AboutPageView, publicbarcode, success, error

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("publicbarcode/",  publicbarcode, name="publicbarcode"),
    path("error/",  error, name="error"),
    path("success/", success, name="success"),
]
