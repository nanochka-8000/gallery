from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artwork/<int:pk>/', views.artwork_detail, name='artwork_detail'),
    path('workshop/<int:pk>/', views.workshop_detail, name='workshop_detail'),
    path('workshop-member/<int:pk>/', views.workshop_member_detail, name='workshop_member_detail'),
    path('series/<int:pk>/', views.series_detail, name='series_detail')
]