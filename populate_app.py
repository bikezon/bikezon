import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikezon.settings')

import django 
django.setup()

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
        'description': 'Do not forget to grab both, one is not too useful'} ]

    # data for subcategories of bikes
    bike_subcats = [ {'name': 'MTB', 
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
        {'username': 'Kellie',
        'password': '321',
        'email': 'imnotellie@hello.com'},
        {'username': 'Dellie',
        'password': 'not123',
        'email': 'imightbeellie@hi.com'} ]

    # data for user profiles
    # todo

    # data for products
    # todo

    # data for wishlists
    # todo

    # data for rating
    # todo
    
    for cat_d in categories:
        c = add_category(cat_d['name'], cat_d['description'])
        for sub_d in cat_d['subcats']:
            add_subcat(sub_d['name'], sub_d['description'], c)


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
    u = User.objects.get_or_create(username=username, password=password, 
    email=email)[0]
    u.save()
    return u

# todo those functions
def add_user_profile():
    pass

def add_product():
    pass

def add_productlist():
    pass

def add_rating():
    pass


if __name__ == '__main__':
    print("Starting the population script")
    populate()