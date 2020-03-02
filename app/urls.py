from django.urls import path
from app import views

app_name = 'app'

# TODO add slug mapping to specific items in components and bikes

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('basket', views.basket, name='basket'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('categories', views.categories, name='categories'),
    path('account', views.account, name='account'),
    path('account/wish-list', views.wish_list, name='wish-list'),
    path('account/sell-item', views.sell_item, name='sell-item'),
]
