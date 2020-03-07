from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Category, SubCategory, Product, UserProfile
from app.forms import UserForm, UserProfileForm, ProductForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
import logging
import os

# ----------- Logger config ----------- #
if not os.path.exists("logs/"):
    os.makedirs("logs")

if not os.path.exists("logs/main_logs.log"):
    open("logs/main_logs.log", 'a').close()

logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs/main_logs.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


# ----------- Views follow from design specification ----------- #

def index(request):
    """ handles homepage logic

    Arguments:
        request -- [standard Django request arg]

    Returns:
        render -- renders homepage and context dict
    """
    avatar = None
    user = request.user
    if user:
        if user.is_active:
            profile = UserProfile.objects.get(user=request.user)
            avatar = profile.picture
    else:
        avatar = None

    context_dict = {
        "categories": Category.objects.all(),
        "subcategories": SubCategory.objects.all(),
        "products": Product.objects.all(),
        "picture": avatar,
    }
    logger.info("Index requested with context dict: %s", context_dict)
    return render(request, 'app/index.html', context=context_dict)


def contact(request):
    # temp contact view
    logger.info("Contact requested")
    return render(request, 'app/contact.html')


def user_login(request):
    """ Handles User login logic

    Arguments:
        request -- [standard Django request arg]

    Returns:
        Redirect - on correct login, redirect to homepage
        HttpResponse 1 - if account not found/disabled
        HttpResponse 2 - if wrong details, show message
        Render - failsafe, reload login page
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        logger.info("User: %s is being authenticated", username)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("app:index"))
                logger.info("User: %s is authenticated", username)
            else:
                return HttpResponse("Your Bikezon account is disabled.")
                logger.info("User: %s triggered account disabled", username)
        else:
            messages.error(request, 'username or password not correct')
            logger.info("User: %s failed to authenticate", username)
            return redirect('app:login')
    else:
        logger.info("Rendered login page")
        return render(request, "app/login.html")


def register(request):
    """ Handles user registration logic

    Arguments:
        request -- [standard Django request arg]

    Returns:
        Render - render registration page with appropriate info
    """
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if (user_form.is_valid() and profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if ("picture" in request.FILES):
                profile.picture = request.FILES["picture"]
            profile.save()
            logger.info("User: %s is registered", user)
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
            logger.info("User: failed to register with user form errors: %s \n \
                        and profile form errors: %s", user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        logger.info("Rendered registration page")

    return render(request, "app/register.html",
                  context={"user_form": user_form,
                           "profile_form": profile_form,
                           "registered": registered})


@login_required
def user_logout(request):
    """ Logout logic

    Returns:
        Redirection to homepage
    """
    logger.info("User: %s is logger out", request.user)
    logout(request)
    return redirect(reverse('app:index'))


def show_categories(request):
    """handles displaying all categories

    Arguments:
        request -- [standard Django request arg]

    Returns:
        render -- renders categories through context dict
    """
    context_dict = {}
    category_list = Category.objects.all()
    context_dict['categories'] = category_list
    logger.info("Show categories called with categories: %s",
                context_dict['categories'])
    return render(request, 'app/categories.html', context=context_dict)


def show_category(request, category_name_slug):
    """ handles category page logic

    Arguments:
        request -- [standard Django request arg]
        category_name_slug -- the category name slug, will
        determines the category that displays on page

    Returns:
        rendering of category (to string method)
    """
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None

    logger.info("Show category called with category: %s",
                context_dict['category'])
    return render(request, 'app/category.html', context=context_dict)


def show_sub_category(request, category_name_slug, subcategory_name_slug):
    """ handles sub_category page logic

    Arguments:
        request -- [standard Django request arg]
        sub_category_name_slug -- the sub_category name slug, will
        determines the sub_category that displays on page

    Returns:
        rendering of sub_category (to string method)
    """
    context_dict = {}
    try:
        category = SubCategory.objects.get(slug=subcategory_name_slug)
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None

    logger.info("Show sub category called with sub category: %s",
                context_dict['category'])
    return render(request, 'app/category.html', context=context_dict)


def product(request, product_name_slug):
    """ handles product page logic

    Arguments:
        request -- [standard Django request arg]
        product_name_slug -- the product name slug, will
        determines the product that displays on page

    Returns:
        rendering of product (to string method)
    """
    context_dict = {}
    try:
        product = Product.objects.get(slug=product_name_slug)
        print(product)
        print("check")
        context_dict['product'] = product

    except Product.DoesNotExist:
        context_dict['product'] = None

    logger.info("Show product called with product: %s",
                context_dict['product'])
    return render(request, 'app/product.html', context=context_dict)


@login_required
def wish_list(request):

    avatar = None
    user = request.user
    if user:
        if user.is_active:
            profile = UserProfile.objects.get(user=request.user)
            avatar = profile.picture
    else:
        avatar = None

    context_dict = {
        "picture": avatar,
    }
    logger.info("Rendering wish list")
    return render(request, 'app/list.html', context=context_dict)


@login_required
def account(request):
    avatar = None
    user = request.user
    if user:
        if user.is_active:
            profile = UserProfile.objects.get(user=request.user)
            avatar = profile.picture
    else:
        avatar = None

    context_dict = {
        "picture": avatar,
    }
    logger.info("Rendering account")
    return render(request, 'app/account.html', context=context_dict)


@login_required
def sell(request):
    """ Handles adding a new product by user

    Arguments:
        request -- [standard Django request arg]

    Returns:
        redirect -- on success go back to home page
        render -- render the sell html page with correct f
    """
    if request.method == "POST":
        post_data = request.POST.dict()
        profile = UserProfile.objects.get(user=request.user)
        post_data['seller'] = profile
        product_form = ProductForm(request.POST, request.FILES, post_data)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.seller = profile
            product.save()
            logger.info("Product registered (sell): %s", product)
            return redirect(reverse("app:index"))
        else:
            print(product_form.errors)
            logger.info("Product registered (sell) failed: %s",
                        product_form.errors)
    else:
        product_form = ProductForm()
        logger.info("Product form rendered")

    return render(request, "app/sell.html",
                  context={"form": product_form, })


@login_required
def edit_profile(request):
    form = EditProfileForm(request.POST, request.FILES or None)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES or None)
        if form.is_valid():
            obj = UserProfile.objects.get(user=request.user)
            obj.user_picture = form.cleaned_data['picture']
            obj.address = form.cleaned_data['address']
            obj.phone = form.cleaned_data['phone']
            obj.save()

            return redirect('app:account')
        else:
            print(form.errors)

    avatar = None
    user = request.user
    if user:
        if user.is_active:
            profile = UserProfile.objects.get(user=request.user)
            avatar = profile.picture
    else:
        avatar = None
    context_dict = {'form': form, 'picture': avatar}

    return render(request, 'app/edit_profile.html', context_dict)


# ----------- Error handler views ----------- #

def handler404(request, exception):
    # temp 404 handler
    logger.info("404 page hit")
    return render(request, 'app/handler404.html', status=404)


def handler500(request):
    # temp 500 handler
    logger.info("500 page hit")
    return render(request, 'app/handler500.html', status=500)
