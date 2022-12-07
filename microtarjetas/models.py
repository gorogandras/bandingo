from django.db import models

# Create your models here.
class Card(models.Model):
    word_en = models.CharField(max_length = 30)
    word_es = models.CharField(max_length = 30)
    
    def get_absolute_url(self):
        return "/cards"

    def __str__(self):
        return f"{self.word_en} --- {self.word_es}"


