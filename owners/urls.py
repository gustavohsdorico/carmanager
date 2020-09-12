from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .api.viewsets import OwnerViewSet, OwnerCreateViewSet, OwnerDocViewSet,
from vehicles.api.viewsets import VehicleListViewSet, VehicleCreateViewSet, VehiclePlateListViewSet

urlpatterns = [
    url(r'^auth/', obtain_jwt_token),
    ##Owner
    #Listar
    url(r'^proprietario/', OwnerViewSet.as_view({'get': 'list'})),
    #Criar
    url(r'^criar/proprietario/', OwnerCreateViewSet.as_view({'post': 'create'})),
    #Buscar por documento
    url(r'^doc/proprietario/(?P<doc>\w+)$', OwnerDocViewSet.as_view({'get': 'list'})),

    #Vehicle
    #Listar
    url(r'^veiculos/', VehicleListViewSet.as_view({'get': 'list'})),
    #Criar
    url(r'^criar/veiculos/', VehicleCreateViewSet.as_view({'post': 'create'}))
    #Buscar
    url(r'^placa/veiculos/(?P<placa>\w+)$', VehiclePlateListViewSet.as_view({'get': 'list'})),
]
