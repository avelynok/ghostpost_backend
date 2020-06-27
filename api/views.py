from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializer import PostSerializer
from g_post.models import Post
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    queryset = Post.objects.all().order_by('-date')
    
    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(post_type=True).order_by('-date')
        page = self.paginate_queryset(boast)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.boast)
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(post_type=False).order_by('-date')
        page = self.paginate_queryset(roast)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.roast)
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def upVote(self, request, pk=id):
        post = Post.objects.get(pk=pk)
        post.upVote += 1
        post.totalVote +=1
        post.save()
        return Response({'status': 'Upvoted'})
    
    @action(detail=True, methods=['get'])
    def downVote(self, request, pk=id):
        post = Post.objects.get(pk=pk)
        post.downVote += 1
        post.totalVote -=1
        post.save()
        return Response({'status': 'Downvoted'})
        
    @action(detail=False)
    def totalVote(self, request):
        totalVote = Post.objects.all().order_by('-totalVote')
        serializer = self.get_serializer(totalVote, many=True)
        return Response(serializer.data)
    

"""def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                post_type = data['post_type'],
                post = data['post'],
                upVote=0,
                downVote=0
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddPostForm()
    return render(request, 'AddPostForm.html', {'form': form})"""


