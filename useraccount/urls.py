from django.urls import path
from useraccount.views import login_view, signup_view, my_profile, edit_profile, send_suggestion_email,logout_request

app_name = "user"


urlpatterns =[
    path("login/", login_view, name ="login"),
    path("register/", signup_view, name ="register"),
    #path("send-mail/",send_confirm_email, name ="send-mail"),
    path("my-profile/",my_profile, name ="my_profile"),
    path("edit-profile/",edit_profile, name ="edit_profile"),
    path("send-suggestion-email/<int:id>",send_suggestion_email, name ="send_suggestion_email"),
    path("logout/",logout_request, name ="logout"),
]