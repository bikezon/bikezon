from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# ----------- Views follow from design specification ----------- #

def home(request):
    # temp home view
    return render(request, 'app/home.html')


def contact(request):
    # temp contact view
    return render(request, 'app/contact.html')


def basket(request):
    # temp basket view
    return render(request, 'app/basket.html')


def login(request):
    # temp login view
    return render(request, 'app/login.html')


def register(request):
    # temp register view
    return render(request, 'app/register.html')


def categories(request):
    # temp categories view
    return render(request, 'app/categories.html')


# temp category view for debugging
def category(request):
    # temp categories view
    return render(request, 'app/category.html')


def account(request):
    # temp account view
    return render(request, 'app/account.html')


def wish_list(request):
    # temp wish list view
    return render(request, 'app/wishlist.html')


def sell_item(request):
    # temp sell item view
    return render(request, 'app/sell_item.html')


# ----------- Error handler views ----------- #

def handler404(request, exception):
    # temp 404 handler
    return render(request, 'app/handler404.html', status=404)


def handler500(request):
    # temp 500 handler
    return render(request, 'app/handler500.html', status=500)
