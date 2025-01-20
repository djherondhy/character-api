from rest_framework import generics, permissions
from .models import Personagem
from .serializers import PersonagemSerializer

class PersonagemListCreateView(generics.ListCreateAPIView):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Personagem.objects.filter(created_by=self.request.user)

class PersonagemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Personagem.objects.filter(created_by=self.request.user)

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username e senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return Response({'message': 'Usuário registrado com sucesso'}, status=status.HTTP_201_CREATED)
