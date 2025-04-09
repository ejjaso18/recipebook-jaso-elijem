from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes', default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100, null=True) 
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='recipe')
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='ingredients')
    
    def __str__(self):
        return '{} of {} in {}'.format(self.ingredient.name, self.quantity, self.recipe.name)
    
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_image/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name='images')
    
    def get_absolute_url(self):
        return reverse('image', args=[self.pk])
    



