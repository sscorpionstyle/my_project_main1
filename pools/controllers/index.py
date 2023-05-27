from django.http import HttpResponse
from django.shortcuts import redirect, render
from pools.models import Feedback


def index(request):
    return render(request, "index.html", {})


def aboutAbout(request):
    return render(request, "about.html", {})


def aboutHome(request):
    return render(request, "index.html", {})


def aboutContact(request):
    return render(request, "contact.html", {})

def aboutBasket(request):
    return render(request, "shopping_list.html", {})

def aboutWork(request):
    return HttpResponse("Student")


