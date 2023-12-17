from django.contrib import admin

from .models import coffee

class coffeeadmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')
admin.site.register(coffee,coffeeadmin)
