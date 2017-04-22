from django.contrib import admin

from .models import Adresse, UserProfile, Profile

admin.site.register(Adresse)
admin.site.register(UserProfile)
admin.site.register(Profile)