from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest.models import Info

from rest.serializers import InfoModelSerializer


class InfoModelViewSet(ModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = Info.objects.all() 