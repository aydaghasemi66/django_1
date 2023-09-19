from allauth.account.forms import SignupForm,ChangePasswordForm,LoginForm
from django import forms



class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    phone_number = forms.CharField(max_length=15, label='Phone Number', required=True)
    

    def save(self, request):
   
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.profile.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user


class CustomChangePasswordForm(ChangePasswordForm):
    new_password_confirm = forms.CharField(
        label="Confirm New Password",
        strip=False,  # Remove the strip=False if not needed
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
)

    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        new_password_confirm = forms.CharField(
            label="Confirm New Password",
            strip=False,  # Remove the strip=False if not needed
            widget=forms.PasswordInput(attrs={'class': 'form-control'}),
)


class CustomLoginForm(LoginForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
        label="Remember Me"
    )