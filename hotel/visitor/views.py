from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request, 'index.html')

def hotel(request):
	return render(request, 'hotel.html')


def confirm(request):
	return render(request, 'conformation.html')


def reviews(request):
	reviews = Review.objects.all().order_by('-timestamp')
	return render(request, 'reviews.html', {'reviews' : reviews})

def review(request, review_id):
	review = Review.objects.get(pk=review_id)
	if review != None:
		return render(request, 'review.html', {'review' : review})
	# flash message saying review with that id not found
	return redirect('visitor:reviews')

@login_required
def add_review(request):
	if request.method != 'POST':
		form = ReviewForm()
		return render(request, 'add_review.html', {'form': form})
	form = ReviewForm(request.POST)
	if form.is_valid():
		review = form.save(commit=False)
		review.user = request.user
		review.save()
		return redirect('review',review.id)

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
