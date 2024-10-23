from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Follow

# Serializer para usuários e a criação de senha 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()
        return user

# Serializer para postagens e contar quantos likes tem 
class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'image', 'created_at', 'likes_count')
        read_only_fields = ('author',)  

    def create(self, validated_data):
       
        request = self.context.get('request') 
        validated_data['author'] = request.user 
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
