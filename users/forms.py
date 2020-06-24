from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Inheriting from the default UserCreationForm to add more fields to the form 
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	# the info about the model with which the form would associate
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		
		# the attributes that a certain field should have
		widgets = {
			'username': forms.TextInput(attrs={'autocomplete': 'off'}),
			'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
		}