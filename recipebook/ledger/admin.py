from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = [ProfileInline,]

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]
    search_fields = ('name', )
    ('Details', {
        'ingredients':
        ('name', 'quantity')
    })

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_filter = ('recipe', )

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
