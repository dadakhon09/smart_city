from rest_framework.serializers import ModelSerializer

from app.model import SubCategory


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
