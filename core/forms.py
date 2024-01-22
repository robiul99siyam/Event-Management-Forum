from django import forms
from .models import contactUser  

class ContactForms(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = contactUser
        fields = ['name', 'subject', 'email','description']  

    def save(self, commit=True):
        contact = super().save(commit=False)
        if self.request:
            contact.user = self.request.user
            contact.save()
        return contact


    def __init__(self, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
