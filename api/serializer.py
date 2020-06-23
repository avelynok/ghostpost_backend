from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from g_post.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_title', 'post', 'post_type', 'upVote', 'downVote', 'date', )