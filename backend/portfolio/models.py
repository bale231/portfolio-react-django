from django.db import models

# Create your models here.

## MODELLO PER I PROGETTI
class Progetto(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.TextField()
    link = models.URLField(blank=True, null=True)
    data_pubblicazione = models.DateField()

    def __str__(self):
        return self.titolo
