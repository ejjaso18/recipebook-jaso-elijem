from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from . import models, forms
from .models import Recipe
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_create.html'
    success_url = reverse_lazy('ledger:recipe_create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_form'] = RecipeForm()
        context['ingredient_form'] = IngredientForm()
        context['recipe_ingredient_form'] = RecipeIngredientForm()
        return context
    
    def form_valid(self, form):
        profile = get_object_or_404(models.Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)

        












