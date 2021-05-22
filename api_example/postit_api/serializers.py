from rest_framework import serializers
from .models import Post, Comment, CommentLike, PostLike


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'body', 'created']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    comment_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'created', 'comments', 'comment_count']

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()