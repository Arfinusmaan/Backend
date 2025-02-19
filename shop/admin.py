from django.contrib import admin
from . models import *

# Register your models here.

class Category_Admin(admin.ModelAdmin):
    list_display=('name','image','description')

admin.site.register(Category,Category_Admin)
admin.site.register(Product)

