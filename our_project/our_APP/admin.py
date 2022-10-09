from django import forms
from django.contrib import admin

from .models import users,course

admin .site.register(users)

admin .site.register(course)