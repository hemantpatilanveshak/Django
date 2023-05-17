from django.db import models

# Create your models here.
class Games(models.Model):
    Game_Name = models.CharField(max_length=100)
    Price = models.CharField(max_length=10)
    Ratings = models.CharField(max_length=10)
    Year_Of_Release = models.CharField(max_length=10)
