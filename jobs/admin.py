from django.contrib import admin
from .models import Job


class JobA(admin.ModelAdmin):
    list_display = ("summary", "image")


admin.site.register(Job, JobA)


admin.site.site_header = "Portfolio Bartka"