from django.shortcuts import render
from Event_creation.models import Event_creation_model
from django.views.generic import TemplateView,DetailView


#------------------------ Event Creation all data ------------------->


class EventCreationAll(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['EventData'] = Event_creation_model.objects.all()
        return context

#------------------------------ UserDetailsView -------------------------------------->
class UserDetailsView(DetailView):
    pk_url_kwarg = 'pk'
    template_name = 'details.html'
    model = Event_creation_model


