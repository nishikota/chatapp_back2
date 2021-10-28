from django.contrib import admin
from .models import Room, Talk
# from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

admin.site.register(Talk)
admin.site.register(Room)