from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def home(request):
	return render(request, 'users/index.html', {})


def register(request):

	# handling form submission
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():

			# "form.cleaned_data" is a dictionary that contains the valid, cleaned, user submitted data
			print(form.cleaned_data)
			username = form.cleaned_data.get('username')

			# save the data if the data is valid
			form.save()

			# a flash mesage to provide acknowledgement to the user
			messages.success(request, f'account created for "{username}"')

			# redirect the user to a particular page on successful registration
			return redirect('home')

	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})


# protected view - requires authentication 
@login_required
def profile(request):
	return render(request, 'users/profile.html')