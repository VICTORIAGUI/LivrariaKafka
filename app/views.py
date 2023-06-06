from django.shortcuts import render

# Create your views here.

def home(request): #Função para chamar a home
    return render(request,
     'app/home.html')

def ebook(request): #Função para chamar a página ebook
    return render(request,
     'app/ebook.html')

def infantil(request): #Função para chamar a página infantil
    return render(request,
    'app/infantil.html')

def importados(request): #Função para chamar a página importados
    return render(request,
    'app/importados.html')

def ofertas(request):
    return render(request,
    'app/ofertas.html')

def quemSomos(request):
    return render(request,
    'app/quemSomos.html')