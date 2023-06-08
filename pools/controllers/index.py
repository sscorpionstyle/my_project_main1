from django.http import HttpResponse
from django.shortcuts import redirect, render
from pools.models import Feedback
from pools.models import Items  # new


def index(request):
    items = Items.objects.all()
    return render(request, 'index.html', {'items': items})  # new end

def show_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedback': feedback})

def aboutAbout(request):
    return render(request, "about.html", {})


def aboutContact(request):
    return render(request, "contact.html", {})


def aboutBasket(request):
    return render(request, "shopping_list.html", {})


