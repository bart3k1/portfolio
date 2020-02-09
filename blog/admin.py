from django.contrib import admin
from .models import Blog


class BlogA(admin.ModelAdmin):
    list_display = ("title", "pub_date", "image")


admin.site.register(Blog, BlogA)