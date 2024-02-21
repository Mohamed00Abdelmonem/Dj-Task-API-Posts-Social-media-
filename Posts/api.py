from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Post, Comment

#___________________________________________________________________________________

# test module simple history
def post_history(request, post_id):
    post_instance = Post.objects.get(pk=post_id)
    historical_data = post_instance.history.all()

    context = {
        'post_instance': post_instance,
        'historical_data': historical_data,
    }

    return render(request, 'post_history.html', context)

# ___________________________________________________________________________________


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['user', 'created_at']
    search_fields = ['caption', 'user']

# ___________________________________________________________________________________


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
                                
    def get_object(self):
        post = super().get_object()
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        post.comments = comments
        return post
# ___________________________________________________________________________________

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

   
    #    # Creating a new comment as a reply to an existing comment
    # parent_comment = Comment.objects.get(id=1)
    # new_comment = Comment.objects.create(post=post_instance, user=user_instance, comment="Reply to the parent", reply=parent_comment)

