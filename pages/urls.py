from django.urls import path

from .views import HomePageView, AboutPageView, publicbarcode, success, error, rrecall,modernreader, modernrecall

urlpatterns = [
    path("", publicbarcode, name="publicbarcode"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("publicbarcode/",  publicbarcode, name="publicbarcode"),
    path("error/",  error, name="error"),
    path("success/", success, name="success"),
    path("recall/", rrecall, name="recall"),
    path("modernreader/", modernreader, name="modernreader"),
    path("modernrecall/", modernrecall, name="modernrecall"),
]
