from django.contrib import admin
from .models import Adresse, UserProfile, Profile

class AddresseAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'hous_number' )
	

admin.site.register(Adresse, AddresseAdmin)
admin.site.register(UserProfile)
admin.site.register(Profile)
