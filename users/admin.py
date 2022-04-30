from users.models import User
from django.contrib import admin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ["id","username","first_name","last_name","email","is_staff","is_active","is_manager"]
    search_fields= ["username","first_name","last_name","email"]
    list_filter= ["is_staff","is_active","is_manager"]