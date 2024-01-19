from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, ListView, View, UpdateView, DeleteView
from .forms import UserEventForm
from .models import Event_creation_model, Confirm_Event
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from user_authenticated.forms import UserRegister
from user_authenticated.views import send_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# ------------------- Event Creation Form ----------------------->


class Event_cration_view(FormView,LoginRequiredMixin):
    template_name = "event_creation.html"
    form_class = UserEventForm
    success_url = reverse_lazy("event_creation")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")  
        if User.objects.filter(email=email).exists():
            messages.warning(self.request, "Email already exists!")
        else:
            form.request = self.request
            self.user = form.save()
            if self.request.user.is_staff:
                self.user.save()
                send_email(self.request.user , 'staff.html','Event Forum Staff Email')
            send_email(self.request.user , 'email_creation.html','Event Creation Email')
            messages.success(self.request, "Event Creation Successfully")

        return super().form_valid(form)



class staff_userView(ListView,LoginRequiredMixin):
    template_name = 'staff.html'
    model = Event_creation_model
    context_object_name = 'events'

    def get_queryset(self):
        user = self.request.user 
        if user.is_authenticated and user.is_staff:
    
            queryset = Event_creation_model.objects.filter(user=user)
            print(queryset)
            return queryset



class UpdateViewUser(UpdateView,LoginRequiredMixin):
    template_name = 'event_creation.html'
    model = Event_creation_model
    form_class = UserEventForm

    def form_valid(self,form):
        form.request = self.request
        user = super().form_valid(form)
        self.user = form.save()
        return user
    def get_success_url(self):
        messages.success(self.request,'Event Update succssully !')
        return reverse_lazy('staff')


    
   
@login_required
def confirm_event(request, id):
    event_instance = get_object_or_404(Event_creation_model, pk=id)
    confirm_event = Confirm_Event(user=request.user)
    confirm_event.save()
    confirm_event.save_events.add(event_instance)
    confirm_event.save()

    messages.success(request,"Event confirm Successfully")
    send_email(request.user,'confrim_email.html',"Event Confrim Email")
    event_instance.count += 1
    event_instance.save()
    return redirect("home")




class ProfileViewData(ListView,LoginRequiredMixin):
    template_name = "profile.html"
    model = Event_creation_model

    def get_queryset(self):
        return Confirm_Event.objects.filter(user=self.request.user).values(
            "save_events"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Event_creation_model.objects.filter(
            id__in=self.get_queryset()
        )
        context["time"] = Confirm_Event.objects.filter(user=self.request.user)
        return context



@login_required
def UserDeleteNow(request, id):
    user = Event_creation_model.objects.get(pk=id)
    messages.success(request, "Delete Succeessfully !")
    send_email(request.user,'delete_email.html','Event Delete Successfully')
    user.delete()
    return redirect("home")




class ConfirmDetailListView(ListView,LoginRequiredMixin):
    template_name = 'confrim_user.html'
    model = Confirm_Event
    context_object_name = 'confrim_user'
    def get_queryset(self):
        return Confirm_Event.objects.all()

