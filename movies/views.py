from django.shortcuts import render
from django.http import Http404

# Create your views here.

# Get all the models to use
from .models import Movie

def index(request):
    all_movies = Movie.objects.all()
    return render(request, "movies/index.html", {
        "all_movies": all_movies
    })


def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        raise Http404
    
    return render(request, "movies/movie_detail.html", {
        "title": movie.title,
        "mainactor": movie.mainactor,
        "rating": movie.rating,
        "is_boxofficehit": movie.is_boxofficehit
    })