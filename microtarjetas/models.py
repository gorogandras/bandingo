from django.db import models

# Create your models here.

class Deck(models.Model):
    name = models.CharField(unique=True, max_length = 30)

    def __str__(self):
        return f"{self.name}"

class Card(models.Model):
    word_en = models.CharField(max_length = 30)
    word_es = models.CharField(max_length = 30)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    
    def get_absolute_url(self): #This one serves to redirect to homepage if we submit data
        return "/cards"

    def __str__(self):
        return f"{self.word_en} --- {self.word_es}"
