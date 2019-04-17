from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'index.html')

def hotel(request):
	return render(request, 'hotel.html')


def confirm(request):
	return render(request, 'conformation.html')


def reviews(request):
	return render(request, 'reviews.html')

def signup(request):
    if request.method == 'POST': # If the form has been submitted
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']

            user = User.objects.create_user(username = username, password = raw_password)

            login(request, user)

            return redirect('visitor:index')


    form = UserCreationForm() # An unbound form
    return render(request, 'signup.html', {'form': form})
