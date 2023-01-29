from django.contrib import admin
from .models import Ecommerce

@admin.register(Ecommerce)
class EcommerceAdmin(admin.ModelAdmin):
    list_display = ('id','name','categeory','price','details','image')

