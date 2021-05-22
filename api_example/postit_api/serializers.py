from rest_framework import serializers
from .models import Post, Comment, CommentLike, PostLike

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'created']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'body', 'created']