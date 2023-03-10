from django.contrib import admin
from userinfo.models import user

class User_admin(admin.ModelAdmin):
    list_display = ('name','email','password')
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(user,User_admin)


