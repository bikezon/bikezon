from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Category, SubCategory, Product, UserProfile, ProductList
from app.forms import UserForm, UserProfileForm, ProductForm, EditProfileForm, EditListingForm
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
            if user.username != 'admin':
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
    """ contact page logic

    just renders the contact page,
    all other logic is handled on
    the html page
    """
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
            # check for picture
            if ("picture" in request.FILES):
                profile.picture = request.FILES["picture"]
            profile.save()
            # create wish list for new user
            wish_list = ProductList.objects.create(
                name=user.username, user=profile)
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
        subcats = SubCategory.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['subcats'] = subcats

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['subcats'] = None

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
        context_dict['product'] = product

    except Product.DoesNotExist:
        context_dict['product'] = None

    logger.info("Show product called with product: %s",
                context_dict['product'])

    # if user is not authenticated set to none
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    else:
        profile = None

    # check if user is authed, if yes, they can edit listing
    auth_user = False
    if product:
        if product.seller == profile:
            auth_user = True

    context_dict['auth_user'] = auth_user

    # cache product name to pass to edit listing
    request.session['product_slug'] = product_name_slug

    return render(request, 'app/product.html', context=context_dict)


@login_required
def wish_list(request):
    """ wish list logic, could be used
    for different lists too

    Arguments:
        request -- [standard Django request arg]

    Returns:
        rendering of wish list
    """
    avatar = None
    user = request.user
    if user:
        if user.is_active:
            profile = UserProfile.objects.get(user=request.user)
            product_list = ProductList.objects.get(user=profile)
            products = Product.objects.filter(productlist=product_list)
            avatar = profile.picture
    else:
        avatar = None

    context_dict = {
        "picture": avatar,
        "products": products,
    }
    logger.info("Rendering wish list")
    return render(request, 'app/list.html', context=context_dict)


@login_required
def account(request):
    """ logic to display user's account
    also displays all products that are
    listed under this seller

    Arguments:
         request -- [standard Django request arg]

    Returns:
        rendering with context dict
    """
    avatar = None
    user = request.user
    seller = UserProfile.objects.get(user=user)
    products = Product.objects.filter(seller=seller)
    if user:
        if user.is_active:
            profile = UserProfile.objects.get(user=request.user)
            avatar = profile.picture
    else:
        avatar = None

    context_dict = {
        "picture": avatar,
        "products": products
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
    """ allows a user to edit their profile
    Arguments:
        request -- [standard Django request arg]
    Returns:
        Errors if there were errors with form completion
        Redirect to account
        Or renders the page
    """
    logger.info("Edit profile page hit")
    form = EditProfileForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        logger.info("%s is editing ptofile", request.user)
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


@login_required
def add_to_list(request, product_name_slug):
    """ add/remove a product to a list
    Arguments:
        request -- [standard Django request arg]
        product_name_slug -- slug of product to pass

    Returns:
        Redirect to the product page
    """
    profile = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(slug=product_name_slug)
    if request.method == 'POST':
        product_list = ProductList.objects.get(user=profile)
        if product in product_list.product.all():
            product_list.product.remove(product)
            logger.info("User %s is removing product %s from their list",
                        request.user, product)
        else:
            product_list.product.add(product)
            logger.info("User %s is adding product %s to their list",
                        request.user, product)

    return redirect('app:product', product_name_slug)


@login_required
def feed(request):
    """ handles user follows feed logic
    gets the name of the user, finds users
    that this user follows and then displays 
    the products that those users are selling

    Arguments:
        request -- [standard Django request arg]

    Returns:
        rendered page with appropriate context
    """
    profile = UserProfile.objects.get(user=request.user)
    following = profile.follows
    profiles = []
    for user in following.all():
        profiles.append(user)

    products = {}
    for user in profiles:
        product_list = Product.objects.filter(seller=user)
        products[user] = product_list

    logger.info("Generating feed for: %s", request.user)
    context_dict = {'profiles': profiles, 'products': products}

    return render(request, 'app/feed.html', context=context_dict)


@login_required
def follow_user(request, product_name_slug):
    """ handles logic of following a user
    this view relies on the product seller name
    from the product.html template. It uses
    the seller name to determine the profile
    to follow. 

    Arguments:
        request -- [standard Django request arg]
        product_name_slug -- slug of product to pass to redirect

    Returns:
        redirection to the product page
    """
    owner = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        user_to_follow = request.POST.get('follow_this').split(' ')[1]
        for profile in UserProfile.objects.all():
            if profile.user.username == user_to_follow:
                if not profile in owner.follows.all():
                    owner.follows.add(profile)
                    logger.info("%s followed %s", owner, user_to_follow)
                else:
                    owner.follows.remove(profile)
                    logger.info("%s Unfollowed %s", owner, user_to_follow)

    return redirect('app:product', product_name_slug)


@login_required
def edit_listing(request):
    """ allows a user to edit their profile

    Arguments:
        request -- [standard Django request arg]

    Returns:
        Errors if there were errors with form completion
        Redirect to account
        Or renders the page
    """
    form = EditListingForm()
    if request.method == 'POST':
        form = EditListingForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Product.objects.get(slug=request.session['product_slug'])
            obj.name = form.cleaned_data['name']
            obj.price = form.cleaned_data['price']
            obj.description = form.cleaned_data['description']
            obj.save()
            logger.info("Edited listing for: %s by user: %s.",
                        obs, request.user)
            return redirect('app:index')
        else:
            print(form.errors)

    context_dict = {'form': form}
    logger.info("Rendered edit_listing view.")
    return render(request, 'app/edit_listing.html', context_dict)
    # ----------- Error handler views ----------- #


def handler404(request, exception):
    """ 404 page handler (page not found)
    
    Arguments:
        request - [standard Django request arg]
        exception - exception type (in this case should be 404)
    
    Returns:
        rendering of 404 page
    """
    logger.info("404 page hit")
    return render(request, 'app/handler404.html', status=404)


def handler500(request):
    """ 500 page handler (server error)
    
    Arguments:
        request - [standard Django request arg]
        exception - exception type (in this case should be 404)
    
    Returns:
        rendering of 500 page
    """
    logger.info("500 page hit")
    return render(request, 'app/handler500.html', status=500)
