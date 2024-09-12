from django.contrib import admin
from .models import Profile

list_display = (
    'photo', 'name', 'email', 'phone', 'summary', 'degree', 'school', 'university', 'previous_work', 'skills')

admin.site.register(Profile)
