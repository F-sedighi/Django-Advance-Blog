from rest_framework import generics
from django_filters import rest_framework as filters
from ...models import Post
from .serializers import PostSerializer


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Post
        fields = ["category", "in_stock"]


class ProductList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
