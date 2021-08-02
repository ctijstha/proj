from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from useraccount.models import Profile

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = "Your Password"
        self.fields["username"].widget.attrs["placeholder"] = "username"
        
    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        #if len(password) < 10:
        #    raise ValidationError("Password must contain at least 10 characters.")
        #return password
        
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
        
    
    def save(self, commit=True):
        user = super(CustomSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        
        if commit:
            user.save()
            
        return user

class ProfileEditForm(forms.ModelForm):
    contact = forms.CharField(max_length=10)
    email = forms.EmailField()
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["contact"].help_text = "Your contact information"   
        
    class Meta:
        model = Profile
        fields = ["contact","email",]