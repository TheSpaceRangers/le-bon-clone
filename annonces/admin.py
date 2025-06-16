from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Category, Listing

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Listing)
