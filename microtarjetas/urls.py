from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('cards/', views.CardsView.as_view(), name='cards'),
    path('cards/new', views.CreateCardView.as_view(), name='create_card'),
    path('cards/<pk>/delete/', views.DeleteCardView.as_view(), name='delete_card'),
    path('cards/<pk>/update/', views.UpdateCardView.as_view(), name='update_card'),
    path('decks/', views.DecksView.as_view(), name='decks'),
    path('decks/new', views.CreateDeckView.as_view(), name='create_deck'),
]