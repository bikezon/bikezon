import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikezon.settings')
django.setup()
from django.core.files import File
from app.models import Category, SubCategory, Product, ProductList, Rating, UserProfile
from django.contrib.auth.models import User

def populate():
    # data for subcategories of components
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

    # data for subcategories of bikes
    bike_subcats = [{'name': 'MTB',
                     'description': 'Because risk is in your blood'},
                    {'name': 'Road bike',
                     'description': 'Public transport is expensive after all'},
                    {'name': 'Hybrid',
                     'description': 'Why not both'}]

    # data for categories
    categories = [
        {'name': 'Components',
         'description': 'All the parts of bike you will need!',
         'subcats': comp_subcats},
        {'name': 'Bikes',
         'description': 'Ready to go bike if you are feeling lazy',
         'subcats': bike_subcats}]

    # data for users
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

    # data for user profiles
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
         'stars': 3}
    ]

    # data for products
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
    # todo

    # data for rating
    # todo

    # Create superuser
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

    # Populate users and user profiles
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
        # Add each user followed
        for f in following:
            followed = None
            for temp in UserProfile.objects.all():
                if temp.user.username == f:
                    followed = temp
                    break
            owner.follows.add(followed)

    for product in products:
        # Get the seller object
        seller = None
        for s in UserProfile.objects.all():
            if s.user.username == product['seller']:
                seller = s

        subcat = SubCategory.objects.get(name=product['subcategory'])
        '''for s in SubCategory.objects.all():
            if s.name == product['subcategory']:
                subcat = s'''

        p = add_product(subcat, product['name'], product['description'],
                        product['price'], product['picture'], seller)
    # todo call all other populate functions


def add_category(name, descr):
    c = Category.objects.get_or_create(name=name, description=descr)[0]
    c.save()
    return c


def add_subcat(name, descr, cat):
    c = SubCategory.objects.get_or_create(name=name, description=descr,
                                          category=cat)[0]
    c.save()
    return c


def add_user(username, password, email):
    u = User.objects.create_user(
        username=username, email=email, password=password)

    return u

# todo those functions


def add_user_profile(user, picture, phone, address, stars):
    up = UserProfile.objects.create(
        user=user, phone=phone, address=address, stars=stars)
    up.picture.save(picture, File(open(picture, 'rb')))
    return up


def add_product(subcat, name, descr, price, picture, seller):
    p = Product.objects.create(
        name=name, description=descr, price=price, seller=seller)

    p.picture.save(picture, File(open(picture, 'rb')))
    p.subcategory.add(subcat)

    return p


def add_productlist():
    pass


def add_rating():
    pass


if __name__ == '__main__':
    print("Starting the population script")
    populate()
