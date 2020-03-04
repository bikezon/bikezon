from django.contrib import admin
from app.models import Category, UserProfile, Rating, ProductList, Product, \
    SubCategory


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'description')


admin.site.register(Rating)
admin.site.register(SubCategory)
admin.site.register(ProductList)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
