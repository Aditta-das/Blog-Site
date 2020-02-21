from django.contrib import admin
from .models import User
class Admin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username',)
admin.site.register(User, Admin)