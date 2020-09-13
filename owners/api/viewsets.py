from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from owners.models import Owner
from .serializers import OwnerCreateSerializer


class OwnerViewSet(ModelViewSet):
    # Listar
    queryset = Owner.objects.all()
    serializer_class = OwnerCreateSerializer


class OwnerCreateViewSet(ModelViewSet):
    #Criar
    queryset = Owner.objects.all()
    serializer_class = OwnerCreateSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.user).first()
        request.data.update({'user': user.id})
        super(OwnerCreateViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)


class OwnerSearchViewSet(ModelViewSet):
    #Buscar
    serializer_class = OwnerCreateSerializer
    lookup_field = 'doc'

    def get_queryset(self):
        return Owner.objects.filter(doc_number=self.kwargs['doc'])

