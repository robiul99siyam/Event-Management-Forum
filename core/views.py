from django.shortcuts import render
from Event_creation.models import Event_creation_model
from django.views.generic import TemplateView, DetailView, FormView
from .forms import ContactForms
from django.urls import reverse_lazy

# ------------------------ Event Creation all data ------------------->


class EventCreationAll(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["EventData"] = Event_creation_model.objects.all()
        return context


# ------------------------------ UserDetailsView -------------------------------------->
class UserDetailsView(DetailView):
    pk_url_kwarg = "pk"
    template_name = "details.html"
    model = Event_creation_model


class About(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Event"] = Event_creation_model.objects.all()
        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForms
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        form.request = self.request
        self.user = form.save()
        response = super().form_valid(form)
        return response
