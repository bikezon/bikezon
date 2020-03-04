from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from app.models import Category, SubCategory, Product


# ----------- Views follow from design specification ----------- #

def index(request):
    context_dict = {
        "categories" : Category.objects.all(),
        "subcategories" : SubCategory.objects.all(),
        "puroducts" : Product.objects.all(),
    }
    return render(request, 'app/index.html', context=context_dict)


def contact(request):
    # temp contact view
    return render(request, 'app/contact.html')


def login(request):
    # temp login view
    return render(request, 'app/login.html')


def register(request):
    # temp register view
    return render(request, 'app/register.html')


# temp category view for debugging
def category(request):
    # temp categories view
    return render(request, 'app/category.html')


def subcategory(request):
    # temp categories view
    return render(request, 'app/subcategory.html')


def product(request):
    # temp categories view
    return render(request, 'app/product.html')


def list(request):
    # temp categories view
    return render(request, 'app/list.html')


def account(request):
    # temp account view
    return render(request, 'app/account.html')


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
