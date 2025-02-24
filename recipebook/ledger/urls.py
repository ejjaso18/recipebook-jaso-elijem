from django.urls import path
from .views import recipes

urlpatterns = [
    path('recipes', recipes, name='recipes'),
]

app_name = "ledger"