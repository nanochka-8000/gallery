from django.urls import path
from . import views

urlpatterns = [
    path('<int:artwork_pk>/', views.inquiry, name='inquiry'),
]