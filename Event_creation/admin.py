from django.contrib import admin
from .models import Event_creation_model,Confirm_Event




#-------------------- admin model now ----------------------->

class EventCreationAdmin(admin.ModelAdmin):
    list_display = ['event_name','date','time','event_type','description','location']
admin.site.register(Event_creation_model,EventCreationAdmin)
admin.site.register(Confirm_Event)
