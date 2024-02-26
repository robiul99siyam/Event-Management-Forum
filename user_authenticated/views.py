from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView, TemplateView
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response





# -------------------------------- send the email -------------------->


def send_email(user, template, subject):
    message = render_to_string(
        template,
        {
            "user": user,
        },
    )
    send_mail = EmailMultiAlternatives(subject, "", to=[user.email])
    send_mail.attach_alternative(message, "text/html")
    send_mail.send()


# --------------- register form views ----------------------------->
def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            print("User object before save:", user)
            # user.is_active = False
            # user.save()
            print("User object after save:", user)

 
           
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"https://event-management-forum-36ct.onrender.com/user/active/{uid}/{token}"
            print(confirm_link)
            email_subject = "Confirm Your Email"
            email_body = render_to_string('active.html', {'confirm_link' : confirm_link})
 
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            messages.success(request, "We have send you an confirmation email.")
            return redirect('login')
 
    else:
        register_form =UserRegisterForm()
    return render(request, 'UserResgister.html', {'form' : register_form, 'type' : 'Register'})
 
 
class RegisterView(FormView):
    template_name = "UserResgister.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Register Successfully !")
        login(self.request, user)
        send_email(self.request.user, "email_singup.html", "Sing Up Successfully! ")
        return super().form_valid(form)


#------------------------------- user active ------------------>
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
 
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

# ------------------------------ User login View ------------------------->


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        messages.success(self.request, "Logged In Successfully !")
        send_email(self.request.user, "email_login.html", "LogIn Successfully Email")
        return reverse_lazy("home")


# ---------------------- User Logout View ----------------------------->


@login_required
def UserLogOutView(request):
    logout(request)
    messages.success(request, "Logged out Successfully !")
    return redirect("home")


# --------------------- Update profile in user ------------------->


class Userupdate(UpdateView):
    model = User
    template_name = "update_profile.html"
    form_class = UserRegisterForm
    pk_url_kwarg = "id"

    def get_success_url(self):
        messages.success(self.request, "profile update successfully")
        return reverse_lazy("home")

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
