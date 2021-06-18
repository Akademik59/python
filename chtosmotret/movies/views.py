from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Genre, Category
from.forms import ReviewForm


class GenreMovies:
    """Жанры фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_category_new(self):
        return Category.objects.filter(id=2)

    def get_category_popular(self):
        return Category.objects.filter(id=1)

class MoviesView(GenreMovies, ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/index.html"


class MovieDetailView(GenreMovies, DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = 'id'
    template_name = "movies/movie.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class GanresMoviesView(GenreMovies, ListView):
    """Фильтр фильмов по жанрам"""
    template_name = "movies/category.html"
    paginate_by = 1
    def get_queryset(self):
        queryset = Movie.objects.filter(genres__in=self.request.GET.getlist("genre")).order_by('-id').distinct()
        return queryset
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context


class CategoryMoviesView(GenreMovies, ListView):
    """Фильтр фильмов по категориям"""
    template_name = "movies/category.html"
    paginate_by = 1
    def get_queryset(self):
        queryset = Movie.objects.filter(category__in=self.request.GET.getlist("category")).order_by('-id').distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        return context


class Search(GenreMovies, ListView):
    """Поиск фильмов"""
    template_name = "movies/category.html"
    paginate_by = 10
    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        a = "".join(q[0].upper()) + q[1:]
        return Movie.objects.filter(title__icontains=a)
