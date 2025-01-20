from django.db import models

# Create your models here.
class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    forca = models.IntegerField(default=1)
    imagem = models.CharField(max_length=500)

    def __str__(self):
        return self.nome