from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def hotel(request):
	return render(request, 'hotel.html')



def confirm(request):
	return render(request, 'conformation.html')




	
def reviews(request):
	return render(request, 'reviews.html')