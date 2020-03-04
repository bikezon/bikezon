from django.contrib import admin
from app.models import Category, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
