from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from app.category.serializers import CategorySerializer
from app.model import Category


class CategoryCreate(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoriesList(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryList(ListAPIView):
    lookup_field = 'id'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.get(id=self.kwargs['id'])


class CategoryUpdate(UpdateAPIView):
    lookup_field = 'id'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.get(id=self.kwargs['id'])


class CategoryDelete(DestroyAPIView):
    lookup_field = 'id'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.get(id=self.kwargs['id'])
