from rest_framework import serializers
from .models import Personagem

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = ['id', 'nome', 'classe', 'forca', 'imagem']
        