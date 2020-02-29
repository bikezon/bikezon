from django.shortcuts import render
from django.http import HttpResponse


# ----------- Views follow from design specification ----------- #

def home(request):
    # temp home view
    return HttpResponse("Temp home page")


def contact(request):
    # temp contact view
    return HttpResponse("Temp contact page")


def basket(request):
    # temp basket view
    return HttpResponse("Temp basket page")


def login(request):
    # temp login view
    return HttpResponse("Temp login page")


def register(request):
    # temp register view
    return HttpResponse("Temp register page")


def categories(request):
    # temp categories view
    return HttpResponse("Temp category page")


def account(request):
    # temp account view
    return HttpResponse("Temp account view")


def components(request):
    # temp components view
    return HttpResponse("Temp components page")


def bikes(request):
    # temp bikes view
    return HttpResponse("Temp bikes page")


def wish_list(request):
    # temp wish list view
    return HttpResponse("Temp wish list page")


def sell_item(request):
    # temp sell item view
    return HttpResponse("Temp sell item page")


# ----------- Error handler views ----------- #

def handler404(request, exception):
    # temp 404 handler
    return HttpResponse("404 page not found.")
