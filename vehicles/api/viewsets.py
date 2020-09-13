from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from owners.models import Owner
from .serializers import VehicleSerializer
from vehicles.models import Vehicle


class VehicleCreateViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        vehicle = Vehicle.objects.filter(slug=request.data.get('doc')).first()
        owner = Owner.objects.filter(name=request.data.get('owner')).first()
        user = User.objects.filter(username=request.user).first()
        request.data.update({'user': user.id})
        request.data.update({'type': vehicle.id})
        request.data.update({'owner': owner.id})

        super(VehicleCreateViewSet, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)
