from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=255)

class RecipeIngredient(models.Model):
    Quantity = models.BigIntegerField() # not sure
    Ingredient = models.ForeignKey(Ingredient)
    Recipe = models.ForeignKey(Recipe)


