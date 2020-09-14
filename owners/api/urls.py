from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .viewsets import OwnerViewSet, OwnerCreateViewSet, OwnerSearchViewSet


urlpatterns = [
    url(r'^auth/', obtain_jwt_token),

    ##Owner
    #Listar
    url(r'^owner/', OwnerViewSet.as_view({'get': 'list'})),
    #Criar
    url(r'^create/owner/', OwnerCreateViewSet.as_view({'post': 'create'})),
    #Buscar por nome
    url(r'^search/owner/(?P<doc>\w+)$', OwnerSearchViewSet.as_view({'get': 'list'})),
]

