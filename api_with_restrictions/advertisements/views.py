
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from advertisements.models import Advertisement



from advertisements.filters import AdvertisementFilter

from advertisements.serializers import AdvertisementSerializer

from advertisements.permissions import IsCreatorOrStaffOrReadOnly



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    #
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def list(self, request, *args, **kwargs):
        print ("Current user", request.user)
        return super().list(request,*args, **kwargs)




    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy" ]:
            return [IsCreatorOrStaffOrReadOnly()]
        return []

