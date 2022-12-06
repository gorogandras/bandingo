from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('deck/', views.DeckView.as_view(), name='deck'),
]