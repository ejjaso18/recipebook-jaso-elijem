from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from . import models, forms
from .models import Recipe, RecipeImage
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'recipe_create.html'
    
    def get(self, request):
        return render(request, self.template_name, {
            'recipe_form': RecipeForm(),
            'ingredient_form': IngredientForm(),
            'recipe_ingredient_form': RecipeIngredientForm(),
        })
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        if 'recipe' in request.POST:
            print("recipe saved")
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                profile = get_object_or_404(models.Profile, user=request.user)
                recipe.author = profile
                recipe.save()
                print("POST data:", request.POST)
                recipe_ingredient_form = RecipeIngredientForm(initial={'recipe': recipe})
                ingredient_form = IngredientForm()
                return redirect('ledger:recipe_create')
            else:
                ingredient_form = IngredientForm()
                recipe_ingredient_form = RecipeIngredientForm()
        if 'ingredient' in request.POST:
            print("ingredient saved")
            ingredient_form = IngredientForm(request.POST)
            if ingredient_form.is_valid():
                ingredient_form.save()
                print("POST data:", request.POST)
                return redirect('ledger:recipe_create')
            else:
                recipe_form = RecipeForm()
                recipe_ingredient_form = RecipeIngredientForm()
        if 'recipe_ingredient' in request.POST:
            print("recipe ingredient saved")
            recipe_ingredient_form = RecipeIngredientForm(request.POST)
            if recipe_ingredient_form.is_valid():
                recipe_ingredient_form.save()
                print("POST data:", request.POST)
                return redirect('ledger:recipe_create')
            else:
                recipe_form = RecipeForm()
                ingredient_form = IngredientForm()

        return render(request, self.template_name, {
            'recipe_form': recipe_form,
            'ingredient_form': ingredient_form,
            'recipe_ingredient_form': recipe_ingredient_form,
        })
    
class RecipeImageAddView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "recipe_add_image.html"

    def get(self, request, pk):
        recipe = get_object_or_404(models.Recipe, pk=pk)
        return render(request, self.template_name, 
                      {"recipe_add_image_form": RecipeImageForm(),
                       "recipe": recipe
                       })
    
    def post(self, request, pk):
        print(request.POST)
        recipe = get_object_or_404(models.Recipe, pk=pk)
        add_image_form = RecipeImageForm(request.POST, request.FILES)
        # print(request.POST)
        if add_image_form.is_valid():
            # print("gradd")        
            image = add_image_form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe', pk=pk)
        return render(request, self.template_name, {
            "recipe_add_image_form": add_image_form,
            "recipe": recipe
        })
    
    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe_detail',
            kwargs={'pk': self.kwargs['pk']}
        )
            
        












