from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Card
from .forms import CardForm, DeleteCardForm

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
        return context

class CreateCardView(CreateView):
    model = Card
    template_name = 'microtarjetas/add_card.html'
    form_class = CardForm
    success_url = '/cards'

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

    