from django.shortcuts import render,redirect
from django.views.generic import FormView,UpdateView,TemplateView
from .forms import UserRegister
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required





#-------------------------------- send the email -------------------->


def send_email(user,template,subject):
    message = render_to_string(template,{
        "user":user,
    })
    send_mail = EmailMultiAlternatives(subject,'',to=[user.email])
    send_mail.attach_alternative(message,'text/html')
    send_mail.send()

#--------------- register form views ----------------------------->

class RegisterView(FormView):
    template_name = 'UserResgister.html'
    form_class  = UserRegister
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        user = form.save()
        messages.success(self.request,'Register Successfully !')
        login(self.request,user)
        send_email(self.request.user,'email_singup.html','Sing Up Successfully! ')
        return super().form_valid(form)






#------------------------------ User login View ------------------------->
    

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        messages.success(self.request,'Logged In Successfully !')
        send_email(self.request.user,'email_login.html','LogIn Successfully Email')
        return reverse_lazy('home')




#---------------------- User Logout View ----------------------------->



@login_required
def  UserLogOutView(request):
    logout(request)
    messages.success(request,"Logged out Successfully !")
    return redirect('home')




