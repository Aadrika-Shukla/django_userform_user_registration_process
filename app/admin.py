from django.contrib import admin
from app.models import *      # to register our profile table no need to register user table as it it is built in table already registered

# Register your models here.
admin.site.register(Profile)