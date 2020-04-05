from rest_framework.serializers import ModelSerializer

from app.model import Complain


class ComplainSerializer(ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'
