from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Card, Deck
from .forms import CardForm, DeleteCardForm, DeckForm
import random

class HomeView(TemplateView):
    template_name = "microtarjetas/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        return context

class CardsView(ListView):
    model = Card
    template_name = "microtarjetas/cards.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["cards"] = Card.objects.all()
        context['randomcard'] = random.choice(list(Card.objects.all())) #selects a card randomly
        return context

class DecksView(ListView):
    model = Deck
    template_name = "microtarjetas/decks.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["decks"] = Deck.objects.all()
        return context

class CreateCardView(CreateView):
    model = Card
    template_name = 'microtarjetas/add_card.html'
    form_class = CardForm
    success_url = '/cards'


class CreateDeckView(CreateView):
    model = Deck
    template_name = 'microtarjetas/add_deck.html'
    form_class = DeckForm
    success_url = '/decks'

class DeleteCardView(DeleteView):
    model = Card
    template_name = 'microtarjetas/delete_card.html'
    form_class = DeleteCardForm
    success_url = '/cards/'


class UpdateCardView(UpdateView):
    model = Card
    template_name = 'microtarjetas/update_card.html'
    form_class = CardForm
    success_url = '/cards'    

    
class CheckCardView(TemplateView):
    model = Card
    template_name = "microtarjetas/check_card.html"

    def get_context_data(self):
        context = super().get_context_data()
        #context["cards"] = Card.objects.all()
        return context   

class CheckRandomCardView(TemplateView):
    model = Card
    template_name = "microtarjetas/check_random_card.html"
    form_class = CardForm

    def get_context_data(self):
        context = super().get_context_data()
        context['randomcard'] = random.choice(list(Card.objects.all())) #selects a card randomly
        return context   