from django.views.generic import TemplateView
from django.shortcuts import render,redirect

class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def publicbarcode(request):   
    return render(request, 'pages/publicbarcode.html')
def error(request):   
    return render(request, 'pages/error.html')
def success(request):   
    return render(request, 'pages/success.html')
def rrecall(request):   
    return render(request, 'pages/rrecall.html')
def modernreader(request):   
    return render(request, 'pages/modernreader.html')
def modernrecall(request):   
    return render(request, 'pages/modernrecall.html')
def modernbarcode(request):   
    return render(request, 'pages/modernbarcode.html')
def modernsuccess(request):   
    return render(request, 'pages/modernsuccess.html')