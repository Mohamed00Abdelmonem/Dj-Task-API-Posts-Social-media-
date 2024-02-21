from rest_framework import serializers
from .models import Post, Comment


#___________________________________________________________________________________
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'caption', 'image', 'created_at', 'likes']


#___________________________________________________________________________________


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'created_at', 'user']

#___________________________________________________________________________________
        
class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'likes', 'caption', 'image', 'created_at', 'comments']  



#___________________________________________________________________________________
        