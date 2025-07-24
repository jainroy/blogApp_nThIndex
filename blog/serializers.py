from rest_framework import serializers
from .models import Blog
from authentication.models import User

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Blog
        fields = ['title', 'content', 'images', 'videos', 'author', 'created_at', 'updated_at']


class ReportUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=255, 
        min_length=3, 
        help_text="Username of the user to report",
        default="string"
    )