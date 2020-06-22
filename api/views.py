from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializer import PostSerializer
from g_post.models import Post

# Create your views here.
class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    queryset = Post.objects.all()