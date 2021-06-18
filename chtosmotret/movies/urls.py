from django.urls import path

from . import views


urlpatterns = [
    path('', views.MoviesView.as_view(), name="movie_main"),
    path('ganres/', views.GanresMoviesView.as_view(), name='ganres'),
    path('category/', views.CategoryMoviesView.as_view(), name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('<int:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review')
]