from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blog
        fields = ('title', 'description', 'author')


class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'blogs')
