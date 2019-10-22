from django.contrib import admin
from donation.models import *

# Register your models here.
@admin.register(Category, Institution, Donation)
class AuthorAdmin(admin.ModelAdmin):
    pass
