from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.pagination import PageNumberPagination
from .models import Post, Follow
from .serializers import UserSerializer, PostSerializer, LoginSerializer

# Classe para registrar novos usuários
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Classe para login e obtenção do token JWT
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Credenciais inválidas.'}, status=401)

# Classe para CRUD de postagens
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem interagir

# Feed do usuário (mostra postagens dos usuários seguidos)
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination  # Paginação no feed

    def get_queryset(self):
        following = Follow.objects.filter(
            follower=self.request.user
        ).values_list('followed', flat=True)
        return Post.objects.filter(author__in=following).order_by('-created_at')

# Seguir um usuário
class FollowUserView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        followed_user = get_object_or_404(User, id=user_id)  # Usando get_object_or_404
        Follow.objects.get_or_create(follower=request.user, followed=followed_user)
        return Response({'detail': 'Agora você está seguindo'}, status=201)

# Deixar de seguir um usuário
class UnfollowUserView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        followed_user = get_object_or_404(User, id=user_id)  # Usando get_object_or_404
        Follow.objects.filter(follower=request.user, followed=followed_user).delete()
        return Response({'detail': 'Você deixou de seguir'}, status=204)
