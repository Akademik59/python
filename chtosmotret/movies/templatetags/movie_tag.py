from django import template
from django.db.models import Q
from movies import views
from movies.models import Movie, Category


register = template.Library()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movie(count=7):
    """Последние добавленные фильмы"""
    movies = Movie.objects.order_by('-id')[:count]
    return {"last_movies": movies}


@register.inclusion_tag('movies/tags/slider_head.html')
def get_last_slide(count=3):
    """Слайдер для главной страницы"""
    movies = Movie.objects.order_by('-id')[:count]
    return {"last_slide": movies}


@register.inclusion_tag('movies/tags/new_movie.html')
def get_last_new_movie(count=4, name=""):
    """Популярное и новинки на главной стр"""
    movies = Movie.objects.filter(Q(category=2)).order_by('-id')[:count]
    # movies_url = Movie.objects.filter(Q(category=2)).order_by('-id')
    # movies = Movie.objects.order_by('-id')[:count]
    return {"last_new_movie": movies, "name": name, }


@register.inclusion_tag('movies/tags/new_movie.html')
def get_last_popular_movie(count=4, name=""):
    """Популярное и новинки на главной стр"""
    movies = Movie.objects.filter(Q(category=1)).order_by('-id')[:count]
    # movies = Movie.objects.order_by('-id')[:count]
    return {"last_new_movie": movies, "name": name}
