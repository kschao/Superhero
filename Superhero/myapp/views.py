from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    all_movies = Movie.object.all()
    context = {
        'all_movies': all_movies
    }
    return render(request, 'movies/index.html')

    def detail(request, movie_id):
        