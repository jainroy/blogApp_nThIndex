from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer, ReportUserSerializer
from authentication.models import User
from rest_framework import generics
from django.shortcuts import render
import requests
from .pagination import ConditionalPagination
BLACKLIST_THRESHOLD = 3



class BlogListAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = ConditionalPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author__is_active=True).order_by('-updated_at')


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]
    lookup_field = 'id'



class ReportUserAPIView(generics.GenericAPIView):
    serializer_class = ReportUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        
        try:
            user = User.objects.get(username=username)
            user.report_count += 1
            user.save()

            if user.report_count >= BLACKLIST_THRESHOLD:
                user.is_active = False
                user.save()
                return Response({"message": "User has been blacklisted due to multiple reports."}, status=200)

            return Response({"message": "Report submitted successfully."}, status=200)

        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)
        
def blogListView(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs':blogs})