from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from app.complain.serializers import ComplainSerializer
from app.model import Complain


class ComplainCreate(CreateAPIView):
    serializer_class = ComplainSerializer
    queryset = Complain.objects.all()


class ComplainsList(ListAPIView):
    serializer_class = ComplainSerializer
    queryset = Complain.objects.all()


class ComplainList(ListAPIView):
    lookup_field = 'id'
    serializer_class = ComplainSerializer

    def get_queryset(self):
        return Complain.objects.get(id=self.kwargs['id'])


class ComplainUpdate(UpdateAPIView):
    lookup_field = 'id'
    serializer_class = ComplainSerializer

    def get_queryset(self):
        return Complain.objects.get(id=self.kwargs['id'])


class ComplainDelete(DestroyAPIView):
    lookup_field = 'id'
    serializer_class = ComplainSerializer

    def get_queryset(self):
        return Complain.objects.get(id=self.kwargs['id'])
