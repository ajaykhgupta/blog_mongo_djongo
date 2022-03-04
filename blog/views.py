from rest_framework import generics
from blog.serializers import PostSerializer
from blog.models import Post

# Create your views here.

class ListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




