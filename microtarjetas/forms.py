from django import forms
from .models import Card, Deck

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"

class DeleteCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = []


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = "__all__"