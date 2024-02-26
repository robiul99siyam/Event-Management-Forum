from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Apply_Organizer


# ----------------------- User Register Form Now------------------------->
class UserRegisterForm(UserCreationForm):
    apply_organizer = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(attrs={"type": "checkbox"}),
    )

    email = forms.EmailField(max_length=50,required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "apply_organizer",
        ]

    def save(self, commit=True):
        our_user = super().save(commit=False)
        our_user.is_active = False
        if commit:
            our_user.save()
            apply = self.cleaned_data.get("apply_organizer")
            if apply == True:
                Apply_Organizer.objects.create(
                user=our_user,
                apply_organizer=apply,
            )
            return our_user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exist !")
        return email

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != "apply_organizer":
                self.fields[field].widget.attrs.update({"class": "form-control"})
