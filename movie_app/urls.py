from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.get_director_list_view),
    path('directors/<int:id>/', views.get_director_by_id_view),
    path('movies/', views.get_movie_list_view),
    path('movies/<int:id>/', views.get_movie_by_id_view),
    path('reviews/', views.get_review_list_view),
    path('reviews/<int:id>/', views.get_review_by_id_view),
]