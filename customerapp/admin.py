from django.contrib import admin

from .models import Category, Complaint

# Register your models here.

admin.site.register(Category)
admin.site.register(Complaint)
