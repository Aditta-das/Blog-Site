from django.contrib import admin
from .models import *
class Admin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'massage')
    list_display_links = ('id', 'user_id',)
admin.site.register(Comment, Admin)

class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'user_id')
    list_display_links = ('id', 'title',)
admin.site.register(StyleOne, Admin)


