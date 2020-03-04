from django.urls import path
from app import views

app_name = 'app'

# TODO add slug mapping to specific items in components and bikes

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('categories/', views.show_categories, name='categories'),
    # temp category url for debugging
    path('<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('<slug:category_name_slug>/<slug:subcategory_name_slug>/',
         views.show_sub_category, name='subcategory'),
    path('<slug:product_name_slug>/', views.product, name='product'),
    path('account/', views.account, name='account'),
    path('account/<slug:list_name_slug>/', views.wish_list, name='list'),
    path('account/sell-item/', views.sell_item, name='sell_item'),
]
