from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.


def valueandwaste(request):
    """ A view to return the intro page """

    return render(request, 'valueandwaste/intro.html')


def page1module1(request):
    """ A view to return page1 """

    return render(request, 'valueandwaste/page1.html')
    