from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Follow

# Serializer para usuários (com criação segura de senha)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash da senha
        user.save()
        return user

# Serializer para postagens com contagem de likes
class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'image', 'created_at', 'likes_count')
        read_only_fields = ('author',)  # O autor será definido automaticamente

    def create(self, validated_data):
        # Define o autor como o usuário autenticado
        request = self.context.get('request')  # Obtém o request da context
        validated_data['author'] = request.user  # Atribui o autor autenticado
        return super().create(validated_data)

# Serializer para seguir usuários
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('follower', 'followed')

# Serializer para login de usuários
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
