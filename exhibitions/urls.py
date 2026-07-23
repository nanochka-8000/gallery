from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibition_list, name='exhibition_list'),
    path('<int:pk>/', views.exhibition_detail, name='exhibition_detail'),
    # Добавляем новый путь для страницы со всеми работами выставки
    path('<int:pk>/artworks/', views.exhibition_artworks, name='exhibition_artworks'),
]