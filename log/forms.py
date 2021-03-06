from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import requestTable


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class RegistrationForm(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)  # Set the widget to
    # PasswordInput
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Confirm password")  # Set the widget to

    # PasswordInput and
    # set an appropriate
    # label
    # captcha = CaptchaField()

    # clean_<fieldname> method in a form class is used to do custom validation
    # for the field.
    # We are doing a custom validation for the 'password2' field and raising
    # a validation error if the password and its confirmation do not match
    def clean_password2(self):
        password = self.cleaned_data['password']  # cleaned_data dictionary has the
        # the valid fields
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
                             required=True)
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password1 = forms.CharField(label="Password", max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    password2 = forms.CharField(label="Confirm Password", max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EventForm(forms.ModelForm):
    block = forms.CharField(widget=forms.HiddenInput())
    room_number = forms.CharField(label='ROOM NUMBER', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'room_number'}))
    booking_status = forms.CharField(widget=forms.HiddenInput())
    startDateTime = forms.CharField(label='START DATE', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'startDateTime'}))
    endDateTime = forms.DateTimeField(label='END DATE', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'endDateTime'}))
    description = forms.CharField(label='DESCRIPTION', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter the description for the event'}))
    granter = forms.CharField(label='GRANTER', max_length=30,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'granter'}))
    reserved_by = forms.CharField(label='RESERVED BY', max_length=30,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'reserved_by'}))

    class Meta:
        model = requestTable
        fields = ("description", "granter", "reserved_by","startDateTime","endDateTime","room_number")

    def save(self, commit=True):
        form = super(EventForm, self).save(commit=False)
        if commit:
            form.save()
        return form
