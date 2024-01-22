from django.contrib import admin

from .models import contactUser


class contactAdmin(admin.ModelAdmin):
    list_display =['registerUser','name','email','subject','description']
    def registerUser(self,obj):
        return obj.user.username
admin.site.register(contactUser,contactAdmin)
