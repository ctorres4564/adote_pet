from django.db import models

class NomePet(models.Model):
    nome = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    cliques = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

