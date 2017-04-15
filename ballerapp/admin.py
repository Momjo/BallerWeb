from django.contrib import admin

from .models import Adresse, UserProfile

admin.site.register(Adresse)
admin.site.register(UserProfile)