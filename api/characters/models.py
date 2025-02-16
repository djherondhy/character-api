from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    forca = models.IntegerField(default=1)
    imagem = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome