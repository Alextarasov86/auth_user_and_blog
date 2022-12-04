from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import action
from .permissions import CanDeleteArticle, CanAddArticle, CanChangeArticle
from .serializers import *
from .models import Article, Comment
from rest_framework.response import Response


class ArticlesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, pk=None):
        article = Article.objects.get(pk=pk)

        return Response({
            'result': ArticleWithCommentsSerializer(article).data
        })


class CommentsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except:
            return Response({}, status=404)

        if not request.user.is_superuser:
            if comment.author.id != request.user.id:
                return Response({}, status=403)
        
        comment.delete()

        return Response({})


    @action(detail=False, methods=['get'], url_path='my')
    def get_my_comments(self, request):
        comments = Comment.objects.filter(author=request.user)
        return Response({
            'result': CommentSerializer(comments, many=True).data
        })







