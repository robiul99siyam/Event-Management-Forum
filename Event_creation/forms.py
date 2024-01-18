from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .constant import EVENT_TYPE_CHOICES
from .models import Event_creation_model


class UserEventForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "Time"}))

    class Meta:
        model = Event_creation_model
        fields = [
            "event_name",
            "event_category",
            "date",
            "time",
            "location",
            "description",
            "event_type",
        ]

    def save(self, commit=True):
        event = super().save(commit=False)
        if commit:
            event.user = self.request.user 
            event.save()
        return event


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})