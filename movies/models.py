from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

from django.urls import reverse

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    mainactor = models.CharField(max_length=50, null=True)
    is_boxofficehit = models.BooleanField(default=False)

    def __str__(self):
        return f"(Title: { self.title } Rating: { self.rating })"
    
    def get_absolute_url(self):
        return reverse("movie-detail", args=[self.id])
