from django.contrib import admin
from .models import Products, Producers, Categories
# Register your models here.

admin.site.register(Products)
admin.site.register(Producers)
admin.site.register(Categories)