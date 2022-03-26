import email
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Username', 'id' : 'floatingInput'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email', 'id' : 'floatingInput'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':  'Password', 'id' : 'floatingPassword'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Username','id' : 'floatingInput'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':  'Password','id' : 'floatingInput'}))

class RecommendForm(forms.Form):
    budget = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Budget', 'id' : 'floatingInput', 'type': 'number'}))
    choice = forms.ChoiceField(choices = (("1", "Gaming"), ("2", "Streaming"), ("3", "Office")), widget= forms.RadioSelect(attrs={'id' : 'FloatingInput'}))