from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from g_post.models import Post


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_title', 'post', 'post_type', 'upVote', 'downVote', 'totalVote', 'date', )