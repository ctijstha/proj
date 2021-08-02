from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.template.loader import  render_to_string

from useraccount.forms import CustomSignupForm, ProfileEditForm
from useraccount.models import *
from bmi.models import Suggestion, Userdata

def login_view(request):
    form = AuthenticationForm(request.POST or None)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("bmi:bmi_list"))
        else:
            messages.error(request, form.get_initial_for_field)
            return HttpResponseRedirect(reverse("user:login"))
    context = {"form": form}
    return render(request, "login.html",context)

def signup_view(request):
    # form = UserCreationForm(request.POST or None)
    form = CustomSignupForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:login"))
    
    context ={"form":form}
    return render(request,"register.html",context)

# def send_confirm_email(request):
#     subject = "Test Subject"
#     message = "Test Message"
#     from_email ="ytddash@gmail.com"
#     recipient_list =[
#         "chitij165@gmail.com"
#     ]
#     context = {"name": "Kshitiz"}
#     html_message = render_to_string("test.html", context)
#     res = send_mail(subject,message,from_email, recipient_list, html_message=html_message)
#     return HttpResponse(res)

def send_suggestion_email(request, *args, **kwargs):
    subject = "Suggestion from BMI calculator"
    id = kwargs.get("id")
    user_data = Userdata.objects.get(id=id, user=request.user)
    suggestion = Suggestion.objects.get(category=user_data.bmi_category)
    from_email ="ytddash@gmail.com"
    recipient_list = [request.user.email]
    #recipient_list = ["anup.singh2071@gmail.com", request.user.email]
    context = {"category": suggestion.category, "suggestion": suggestion.message}
    html_message = render_to_string("suggestion.html", context)
    res = send_mail(subject,suggestion.message,from_email, recipient_list, html_message=html_message)
    if res:
        return render(request,"bmi_list.html",{"message": f"Email has been sent to {request.user.email}. Please check your mail"})
    return render(request,"bmi_list.html",{"message": f"Email could not be sent. Please try again."})


def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    email = profile.email
    
    if not email:
        profile.email = request.user.email
        profile.save()
    
    context = {"profile": profile}
    return render(request, 'my_profile.html',context)

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:my_profile"))
    context ={"form":form}
    return render(request,"edit_profile.html",context)

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse("user:login"))