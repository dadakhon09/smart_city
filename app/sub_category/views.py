from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from app.sub_category.serializers import SubCategorySerializer
from app.model import SubCategory


class SubCategoryCreate(CreateAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class SubCategoriesList(ListAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class SubCategoryList(ListAPIView):
    lookup_field = 'id'
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.get(id=self.kwargs['id'])


class SubCategoryUpdate(UpdateAPIView):
    lookup_field = 'id'
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.get(id=self.kwargs['id'])


class SubCategoryDelete(DestroyAPIView):
    lookup_field = 'id'
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.get(id=self.kwargs['id'])
