from django.contrib import admin
from .models import UserProfile
# Register your models here.



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('_id','name', 'email', 'bio', 'created_at')
    search_fields = ('name', 'email','bio')

# Alternatively, you can register the model using the admin.site.register method:
admin.site.register(UserProfile, UserProfileAdmin)
