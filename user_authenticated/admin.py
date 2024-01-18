from django.contrib import admin
from .models import Apply_Organizer
# Register your models here.
class ApplyAdmin(admin.ModelAdmin):
    list_display =['apply_name']
    def apply_name(self,obj):
        return f" Applyed User Name : {obj.user.username} "
admin.site.register(Apply_Organizer,ApplyAdmin)



