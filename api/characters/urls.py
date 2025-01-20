from django.urls import path
from .views import PersonagemListCreateView, PersonagemDetailView, RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', PersonagemListCreateView.as_view(), name='character-list-create'),
    path('<int:pk>/', PersonagemDetailView.as_view(), name='character-detail'),
]