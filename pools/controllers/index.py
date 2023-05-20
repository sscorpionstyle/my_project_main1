from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return render(request, "index.html", {})

def about(request):
    return HttpResponse("My name is Anzhelika")

def aboutWork(request):
    return HttpResponse("Student")

def aboutCoockies(request):
    return HttpResponse("Печеньки")

def aboutCandies(request):
    return HttpResponse("Конфетки")

def aboutLollipop(request):
    return HttpResponse("Леденцы")

def aboutGum(request):
    return HttpResponse("Жвачки")

def aboutEating(request):
    return HttpResponse("Кушоть сладкое вредно")
