from rest_framework import serializers
from .models import *
from users.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ArticleWithCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    # comments = UserSerializer(read_only=True, many=True)
    author = serializers.SerializerMethodField()

    def get_comments(self, article):
        comments = Comment.objects.filter(article=article)
        return CommentSerializer(comments, many=True).data

    def get_author(self, article):
        return UserSerializer(article.author).data

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'date_created', 'author', 'comments')
