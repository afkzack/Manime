from django.shortcuts import render, get_object_or_404
from .models import *

def index_view(request):
	return render(request, 'index.html')

def blog_view(request):
	return render(request, 'blog.html')

def home_view(request):
	anime = Anime.objects.all()
	latest_anime = Anime.objects.order_by('-pub_date')[:4]
	context = {'anime':anime, 'latest_anime':latest_anime}
	return render(request, 'home.html', context)

def episode_view(request, anime_id):
	anime = get_object_or_404(Anime, pk=anime_id)
	episode = Episode.objects.filter(anime=anime)
	context = {
	'anime':anime,
	'episode':episode
	}
	return render(request, 'episode.html', context)

def watch_view(request, episode_id):
	episode = get_object_or_404(Episode, pk=episode_id)
	watch = Watch.objects.filter(episode=episode)
	context = {
	'episode':episode,
	'watch':watch
	}
	return render(request, 'watch.html', context)

def search_animes(request):
	if request.method == "POST":
		searched = request.POST['searched']
		animes = Anime.objects.filter(name__contains=searched)
		return render(request, 'search_animes.html', {
			'searched':searched, 
			'animes':animes, 
			})
	else:
		return render(request, 'search_animes.html', {})

def genres_view(request):
	genres = Genre.objects.all()
	context = {
	'genres':genres,
	}
	return render(request, 'genres.html', context)