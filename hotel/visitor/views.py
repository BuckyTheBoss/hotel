from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def index(request):
	return render(request, 'index.html')

def hotel(request):
	return render(request, 'hotel.html')


def confirm(request):
	return render(request, 'conformation.html')


def reviews(request):
	reviews = Review.objects.all().order_by('-timestamp')
	return render(request, 'reviews.html', {'reviews' : reviews, 'title': 'All Reviews'})

def review(request, review_id):
	review = Review.objects.get(pk=review_id)
	if review != None:
		return render(request, 'review.html', {'review' : review})
	# flash message saying review with that id not found
	return redirect('visitor:reviews')

def user_reviews(request, user_id):
	user = User.objects.get(pk=user_id)
	reviews = user.review_set.all()
	return render(request, 'reviews.html', {'reviews' : reviews, 'title': 'Reviews by: {} {}'.format(user.first_name, user.last_name)})

@login_required
def add_review(request):
	if request.method != 'POST':
		form = ReviewForm()
		return render(request, 'add_review.html', {'form': form, 'title' : "Add Review"})
	form = ReviewForm(request.POST)
	if form.is_valid():
		review = form.save(commit=False)
		review.user = request.user
		review.save()
		return redirect('visitor:review',review.id)

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


@login_required
def edit_review(request, review_id):
	review = Review.objects.get(pk=review_id)
	if request.user != review.user:
		#flash message saying "not your review to edit"
		return redirect('visitor:review', review.id)
	if request.method != 'POST':
		form = ReviewForm(instance=review)
		return render(request, 'add_review.html', {'form': form, 'title' : "Edit Review"})
	form = ReviewForm(request.POST, instance=review)
	if form.is_valid():
		review.save()
		return redirect('visitor:review',review.id)
	return redirect('visitor:index')

@login_required
def delete_review(request, review_id):
	review = Review.objects.get(pk=review_id)
	if request.user == review.user:
		review.delete()
		#flash message saying review deleted
		return redirect('visitor:reviews')
	#flash message saying "not your review to delete"
	return redirect('visitor:review', review.id)