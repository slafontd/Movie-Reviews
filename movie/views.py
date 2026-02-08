from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie


def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'name': 'Santiago Lafont Díaz'})
    SearchTerm = request.GET.get('searchMovie')
    if SearchTerm:
        movies = Movie.objects.filter(title__icontains=SearchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': SearchTerm, 'movies': movies})

def about(request):
    #return HttpResponse('<h1>Welcome to About Page</h1>')
    return render(request, 'about.html')    