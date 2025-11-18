from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import status, mixins, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination

"""
data = {
    "id":"1",
    "title":"hello"
}
"""
# Post List api for Function Base View
"""
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def PostList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
"""
# Post List with APIView for Class Base View
'''
class PostList(APIView):
    """getting a list of posts and creating a new posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        """retriveieng a list of posts"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    def post(self, request):
        """creating a post with provided data"""
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''


class PostList(ListCreateAPIView):
    """getting a list of posts and creating a new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    # for GenericAPIView with mixin.ListModelMixin
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """

    # for GenericAPIView
    '''
    def get(self, request):
        """retriveieng a list of posts"""
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data)
    def post(self, request):
        """creating a post with provided data"""
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    '''


# Post deatail api for FBV
"""
@api_view(["GET", "PUT", "DELETE"])
def PostDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        
    #try:
    #    post = Post.objects.get(pk=id)
    #    serializer = PostSerializer(post)
    #    return Response(serializer.data)
    #except Post.DoesNotExist:
    #    return Response({"detail":"post does not exits"}, status = status.HTTP_404_NOT_FOUND)
"""

# Post detail with APIView for CBV
'''
class PostDetail(APIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """retriveing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostDetail.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        """editing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data= request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(request.data)
    def delete(self, request, id):
        """deleting the post object"""
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
'''


class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting detail of the post and edit plus removing it"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    # lookup_field = 'id'

    # for GenericAPIView with mixins
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    """

    # for GenericAPIView
    '''
    def get(self, request, id):
        """retriveing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostDetail.serializer_class(post)
        return Response(serializer.data)
    '''


# ViewSet
'''
class PostViewSet(viewsets.ViewSet):
    """getting a list of posts and creating a new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        pass   
    def retrieve(self, request, pk):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
'''


# ModelViewSet
class PostModelViewSet(viewsets.ModelViewSet):
    """getting a list of posts and creating a new posts"""

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category', 'author', 'status']
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact", "in"],
        "status": ["exact", "in"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination

    @action(methods=["get"], detail=False)
    def get_ok(self, request):
        return Response({"detail": "ok"})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
