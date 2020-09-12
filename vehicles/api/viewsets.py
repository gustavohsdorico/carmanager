from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from owners.models import Owner
from .serializers import OwnerSerializer


class OwnerCreateViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerRegisterSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.user).first()
        request.data.update({'user': user.id})
        super(OwnerCreateViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

