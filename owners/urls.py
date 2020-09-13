from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .api.viewsets import OwnerViewSet, OwnerCreateViewSet, OwnerSearchViewSet
from vehicles.api.viewsets import VehicleListViewSet, VehicleCreateViewSet, VehiclePlateListViewSet


urlpatterns = [
    url(r'^auth/', obtain_jwt_token),

    ##Owner
    #Listar
    url(r'^owner/', OwnerViewSet.as_view({'get': 'list'})),
    #Criar
    url(r'^create/owner/', OwnerCreateViewSet.as_view({'post': 'create'})),
    #Buscar por nome
    url(r'^search/owner/(?P<doc>\w+)$', OwnerSearchViewSet.as_view({'get': 'list'})),

    #Vehicle
    #Listar
    url(r'^vehicles/', VehicleListViewSet.as_view({'get': 'list'})),
    #Criar
    url(r'^create/vehicles/', VehicleCreateViewSet.as_view({'post': 'create'})),
    #Buscar
    url(r'^search/vehicles/(?P<owner>\w+)$', VehiclePlateListViewSet.as_view({'get': 'list'})),
]
