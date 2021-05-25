from django_filters import rest_framework as filters

from advertisements.models import Advertisement

from advertisements.models import AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ('status', 'created_at', 'updated_at')
