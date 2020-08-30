# from django.contrib.auth import get_user_model
# from django.db.models import Q

# from django import forms


# User = get_user_model()


# class UserCreationForm(forms.ModelForm):
#     # email = forms.EmailField(, required=False)
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Password Confirmation', widget=forms.PasswordInput)
#     # first_name = forms.CharField(label='First name', required=False)
#     # last_name = forms.CharField(label='Last name', required=False)

#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name']

#     def clean_password(self):
#         password1 = self.cleaned_data['password1']
#         password2 = self.cleaned_data['password2']
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords do not match")
#         return password2

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password1'])

#         if commit:
#             user.save()
#         return user


# class UserLoginForm(forms.Form):
#     query = forms.CharField(label='Email or Username')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     def clean(self, *args, **kwargs):
#         query = self.cleaned_data.get('query')
#         password = self.cleaned_data.get('password')
#         user_qs_final = User.object.filter(
#             Q(username__iexact=query) |
#             Q(email__iexact=query)
#         ).distinct()
#         if not user_qs_final.exists() and user_qs_final.count != 1:
#             raise forms.ValidationError(
#                 "Invalid credentials - user doesn't exit")
#         user_obj = user_qs_final.first()
#         if not user_obj.check_password(password):
#             raise forms.ValidationError("Credentials are not correct")
#         self.cleaned_data["user_obj"] = user_obj
#         return super(UserLoginForm, self).clean(*args, **kwargs)

# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth import get_user_model

# from .models import User

User = get_user_model()


class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'placeholder': 'Email..'}), required=True)
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'placeholder': 'Username..'}),  max_length=60, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password..'}))
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput(
            attrs={'placeholder': 'Password confirmation..'}))

    class Meta:
        model = User
        fields = ('username', 'email')

        # def __init__(self, *args, **kwargs):
        #     super(RegisterForm, self).__init__(*args, **kwargs)
        #     for field in self.fields.values():
        #         print(field)
        #         field.widget.attrs['placeholder'] = field.label

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(
        label="Password", max_length=60, required=True)


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
