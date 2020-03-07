from django.urls import path, include
from app import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'app'

# TODO add slug mapping to specific items in components and bikes

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('account/edit_profile', views.edit_profile, name='edit_profile'),
    path('account/sell/', views.sell, name='sell'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('categories/', views.show_categories, name='categories'),
    # slugs
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/<slug:subcategory_name_slug>/',
         views.show_sub_category, name='subcategory'),
    path('product/<slug:product_name_slug>/', views.product, name='product'),
    path('account/wish-list/', views.wish_list, name='list'),
    path('account/<slug:list_name_slug>/', views.wish_list, name='custom-list'),
]
