import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikezon.settings')
django.setup()
from django.core.files import File
from app.models import Category, SubCategory, Product, ProductList, Rating, UserProfile
from django.contrib.auth.models import User


def populate():
    """
    Purpose - Main function used for populating the database.
                Creates a superuser as well as other elements needed in order to
                demonstrate website's functionality.
    Use - populate()
    Throws - n/a
    Returns - n/a
    """
    # Data for subcategories of components
    comp_subcats = [
        {'name': 'Handles',
         'description': 'If you are not ready to go hands free'},
        {'name': 'Tyres',
         'description': 'Cuz you need to roll yo'},
        {'name': 'Seats',
         'description': 'For the real comfiness'},
        {'name': 'Breaks',
         'description': 'Who needs them though, amirite?'},
        {'name': 'Chains',
         'description': 'Yes, bike chains. What were you thinking?'},
        {'name': 'Pedal',
         'description': 'Do not forget to grab both, one is not too useful'}]

    # Data for subcategories of bikes
    bike_subcats = [
        {'name': 'MTB',
         'description': 'Because risk is in your blood'},
        {'name': 'Road bike',
         'description': 'Public transport is expensive after all'},
        {'name': 'Hybrid',
         'description': 'Why not both'}]

    # Data for categories i.e. components and bikes
    categories = [
        {'name': 'Components',
         'description': 'All the parts of bike you will need!',
         'subcats': comp_subcats},
        {'name': 'Bikes',
         'description': 'Ready to go bike if you are feeling lazy',
         'subcats': bike_subcats}]

    # Data for users (8 users)
    users = [
        {'username': 'Ellie',
         'password': '123',
         'email': 'imellie@hello.com'},
        {'username': 'Ellie2',
         'password': '123',
         'email': 'imellie2@hello.com'},
        {'username': 'Ellie3',
         'password': '123',
         'email': 'imellie3@hello.com'},
        {'username': 'Kellie',
         'password': '321',
         'email': 'imnotellie@hello.com'},
        {'username': 'Kellie2',
         'password': '321',
         'email': 'imnotellie2@hello.com'},
        {'username': 'Kellie3',
         'password': '321',
         'email': 'imnotellie3@hello.com'},
        {'username': 'Dellie',
         'password': 'not123',
         'email': 'imightbeellie@hi.com'},
        {'username': 'Bellie',
         'password': '12321',
         'email': 'imightbebellie@hi.com'}]

    # Data for user profiles for each user
    user_profiles = [
        {'username': 'Ellie',
         'picture': 'population_pictures/user_profiles/ellie.jpg',
         'phone': '001',
         'follows': ['Ellie2', 'Ellie3', 'Kellie'],
         'address': 'address of ellie 1',
         'stars': 5},
        {'username': 'Ellie2',
         'picture': 'population_pictures/user_profiles/ellie.jpg',
         'phone': '002',
         'follows': ['Ellie'],
         'address': 'address of ellie 2',
         'stars': 5},
        {'username': 'Ellie3',
         'picture': 'population_pictures/user_profiles/ellie.jpg',
         'phone': '003',
         'follows': ['Ellie'],
         'address': 'address of ellie 3',
         'stars': 5},
        {'username': 'Kellie',
         'picture': 'population_pictures/user_profiles/generic.jpg',
         'phone': '004',
         'follows': ['Kellie2', 'Kellie3', 'Ellie'],
         'address': 'address of kellie',
         'stars': 1},
        {'username': 'Kellie2',
         'picture': 'population_pictures/user_profiles/generic.jpg',
         'phone': '005',
         'follows': ['Kellie'],
         'address': 'address of kellie2',
         'stars': 2},
        {'username': 'Kellie3',
         'picture': 'population_pictures/user_profiles/generic.jpg',
         'phone': '006',
         'follows': ['Kellie'],
         'address': 'address of kellie3',
         'stars': 3},
        {'username': 'Dellie',
         'picture': 'population_pictures/user_profiles/generic.jpg',
         'phone': '007',
         'follows': ['Bellie'],
         'address': 'address of dellie which might be the same as kellies',
         'stars': 4},
        {'username': 'Bellie',
         'picture': 'population_pictures/user_profiles/generic.jpg',
         'phone': '008',
         'follows': ['Dellie'],
         'address': 'address of bellie or so I heard',
         'stars': 3}]

    # Data for products
    products = [
        {'name': 'bike1',
         'subcategory': 'MTB',
         'description': 'bike1',
         'price': 10,
         'picture': 'population_pictures/products/bike1.jpg',
         'seller': 'Ellie'},
        {'name': 'bike2',
         'subcategory': 'MTB',
         'description': 'bike2',
         'price': 203,
         'picture': 'population_pictures/products/bike2.jpg',
         'seller': 'Bellie'},
        {'name': 'bike3',
         'subcategory': 'Hybrid',
         'description': 'bike3',
         'price': 1009,
         'picture': 'population_pictures/products/bike3.jpg',
         'seller': 'Dellie'},
        {'name': 'bike4',
         'subcategory': 'Hybrid',
         'description': 'bike4',
         'price': 76,
         'picture': 'population_pictures/products/bike4.jpg',
         'seller': 'Kellie'},
        {'name': 'road_bike1',
         'subcategory': 'Road bike',
         'description': 'road_bike1',
         'price': 63,
         'picture': 'population_pictures/products/road_bike1.jpg',
         'seller': 'Ellie'},
        {'name': 'road_bike2',
         'subcategory': 'Road bike',
         'description': 'road_bike2',
         'price': 15,
         'picture': 'population_pictures/products/road_bike2.jpg',
         'seller': 'Bellie'},
        {'name': 'road_bike3',
         'subcategory': 'Road bike',
         'description': 'road_bike3',
         'price': 13,
         'picture': 'population_pictures/products/road_bike3.jpg',
         'seller': 'Kellie'},
        {'name': 'road_bike4',
         'subcategory': 'Road bike',
         'description': 'road_bike4',
         'price': 20,
         'picture': 'population_pictures/products/road_bike4.jpg',
         'seller': 'Kellie'},
        {'name': 'pedal1',
         'subcategory': 'Pedal',
         'description': 'pedal1',
         'price': 10,
         'picture': 'population_pictures/products/pedals1.jpg',
         'seller': 'Ellie2'},
        {'name': 'pedal2',
         'subcategory': 'Pedal',
         'description': 'pedal2',
         'price': 60,
         'picture': 'population_pictures/products/pedals2.jpg',
         'seller': 'Ellie2'},
        {'name': 'pedal3',
         'subcategory': 'Pedal',
         'description': 'pedal3',
         'price': 50,
         'picture': 'population_pictures/products/pedals3.jpg',
         'seller': 'Ellie3'},
        {'name': 'pedal4',
         'subcategory': 'Pedal',
         'description': 'pedal4',
         'price': 40,
         'picture': 'population_pictures/products/pedals4.jpg',
         'seller': 'Ellie3'},
        {'name': 'handlebars1',
         'subcategory': 'Handles',
         'description': 'handle1',
         'price': 30,
         'picture': 'population_pictures/products/handlebars1.jpg',
         'seller': 'Kellie2'},
        {'name': 'handlebars2',
         'subcategory': 'Handles',
         'description': 'handle2',
         'price': 10,
         'picture': 'population_pictures/products/handlebars2.jpg',
         'seller': 'Kellie3'},
        {'name': 'handlebars3',
         'subcategory': 'Handles',
         'description': 'handle3',
         'price': 20,
         'picture': 'population_pictures/products/handlebars3.jpg',
         'seller': 'Kellie2'},
        {'name': 'handlebars4',
         'subcategory': 'Handles',
         'description': 'handle4',
         'price': 10,
         'picture': 'population_pictures/products/handlebars4.png',
         'seller': 'Kellie3'}]

    # data for product lists
    wishlists = [
        {'username': 'Ellie',
         'products': ['bike1', 'bike2', 'bike3', 'bike4']},
        {'username': 'Kellie',
         'products': ['pedal1', 'pedal2']},
        {'username': 'Dellie',
         'products': ['road_bike1', 'road_bike2', 'handlebars1']},
        {'username': 'Bellie',
         'products': ['road_bike1', 'handlebars2']}]

    # Create superuser to be accessed with standard login credentials
    try:
        super_user = User.objects.create_superuser(
            username='admin', password='admin', email='bikezon.team@gmail.com')
    except:
        super_user = User.objects.get(username='admin')

    # Populate categories and subcategories
    for cat_d in categories:
        c = add_category(cat_d['name'], cat_d['description'])
        for sub_d in cat_d['subcats']:
            add_subcat(sub_d['name'], sub_d['description'], c)

    # Populate users and user profiles without followers
    for user in users:
        # First create the user
        u = add_user(user['username'], user['password'], user['email'])
        # Then create UserProfile of this user
        for user_prof in user_profiles:
            if user['username'] == user_prof['username']:
                add_user_profile(
                    u, user_prof['picture'], user_prof['phone'], user_prof['address'], user_prof['stars'])
                break

    # Populate the followers for each user profile
    for owner in UserProfile.objects.all():
        following = []

        # Get the list of users followed by the owner
        for user_prof in user_profiles:
            if owner.user.username == user_prof['username']:
                following = user_prof['follows']
                break

        # Add each followed user
        for f in following:
            followed = None
            # Find the user
            for temp in UserProfile.objects.all():
                if temp.user.username == f:
                    followed = temp
                    break
            if followed != None:
                owner.follows.add(followed)

    # Populate the products
    for product in products:
        # Get the seller object
        seller = None
        for s in UserProfile.objects.all():
            if s.user.username == product['seller']:
                seller = s
                break

        subcat = SubCategory.objects.get(name=product['subcategory'])

        p = add_product(subcat, product['name'], product['description'],
                        product['price'], product['picture'], seller)

    # Populate the wishlists
    for wl in wishlists:
        # Get the user profile
        for temp in UserProfile.objects.all():
            if temp.user.username == wl['username']:
                up = temp
                break
        products = []
        # Get the list of product objects
        for p in wl['products']:
            products.append(Product.objects.get(name=p))

        wl = add_productlist(up, products)


def add_category(name, descr):
    """
    Purpose - Create a category in the database
    Use - add_category(name, descr) where name is the category's name 
            and descr is category's description
    Returns - created Category object
    """
    c = Category.objects.get_or_create(name=name, description=descr)[0]
    c.save()
    return c


def add_subcat(name, descr, cat):
    """
    Purpose - Create a subcategory in the database
    Use - add_subcat(name, descr, cat) where name is the subcategory's name, 
            descr is subcategory's description and cat is parent category 
    Returns - created SubCategory object
    """
    c = SubCategory.objects.get_or_create(name=name, description=descr,
                                          category=cat)[0]
    c.save()
    return c


def add_user(username, password, email):
    """
    Purpose - Create a user in the database
    Use - add_user(username, password, email) where username, password and email  
            are user's username, password and email respectively.
    Returns - created User object
    """
    u = User.objects.create_user(
        username=username, email=email, password=password)

    return u


def add_user_profile(user, picture, phone, address, stars):
    """
    Purpose - Create a user profile in the database
    Use - add_user_profile(user, picture, phone, address, stars) where user, picture, phone, address, 
            starts are user profile's user, picture, phone, address and star rating respectively.
    Returns - created UserProfile object
    """
    up = UserProfile.objects.create(
        user=user, phone=phone, address=address, stars=stars)
    up.picture.save(picture, File(open(picture, 'rb')))
    # Create wishlist for every user profile
    wish_list = ProductList.objects.create(name=user.username, user=up)

    return up


def add_product(subcat, name, descr, price, picture, seller):
    """
    Purpose - Create a product in the database
    Use - add_product(subcat, name, descr, price, picture, seller) where subcat, name, descr, price, picture
        and seller are product's subcategory, name, description, price, picture and seller respectively.
    Returns - created Product object
    """
    p = Product.objects.create(
        name=name, description=descr, price=price, seller=seller)

    p.picture.save(picture, File(open(picture, 'rb')))
    p.subcategory.add(subcat)

    return p


def add_productlist(up, products):
    """
    Purpose - Create a product list (e.g. a wishlist) in the database
    Use - add_productlist(up, products) where up is the user profile and
            products is a list of products to be added to the list
    Returns - created ProductList object
    """
    plist = ProductList.objects.get(user=up)
    for p in products:
        plist.product.add(p)

    return plist


# Run the population script only when the module is the main program
if __name__ == '__main__':
    print("Starting the population script")
    populate()
