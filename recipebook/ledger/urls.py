from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageAddView

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/add_image/', RecipeImageAddView.as_view(), name='recipe_add_image'),
]

app_name = "ledger"