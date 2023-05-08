from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class HeaderMediaAdmin(admin.ModelAdmin):

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src = '{object.photo.url}' width=50>")

admin.site.register(HeaderMedia, HeaderMediaAdmin)