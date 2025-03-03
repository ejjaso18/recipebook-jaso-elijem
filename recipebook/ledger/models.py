from django.db import models
from django.urls import reverse

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('Ingredient', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('Recipe', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=10, null=True) 
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='recipes')
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='ingredients')
    


