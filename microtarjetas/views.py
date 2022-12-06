from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

#def home(request):
    #context = {"name":"Bandido"}
    #template = loader.get_template('microtarjetas/home.html')
    #return HttpResponse("Welcome to Microtarjetas")


from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Card

class HomeView(TemplateView):
    template_name = "microtarjetas/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        return context

class DeckView(ListView):
    model = Card
    template_name = "microtarjetas/deck.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["cards"] = Card.objects.all()
        return context