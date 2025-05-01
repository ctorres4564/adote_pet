from django.shortcuts import render
from .models import NomePet
import random

def gerar_nome(request):
    nome = None

    if request.method == "POST":
        nomes_disponiveis = list(NomePet.objects.all())
        if nomes_disponiveis:
            nome = random.choice(nomes_disponiveis)
            nome.cliques += 1
            nome.save()

    return render(request, 'nomes/index.html', {'nome': nome})

