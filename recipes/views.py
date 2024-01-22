from django.shortcuts import render


def index(request):
    return render(request, 'recipes/pages/home.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-page.html')
