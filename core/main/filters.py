import django_filters

from core.main.models.shop_models import Product


class ProductFilter(django_filters.FilterSet):
    material = django_filters.CharFilter(field_name='material', lookup_expr='iexact')
    size = django_filters.CharFilter(field_name='size', lookup_expr='iexact')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['material', 'size', 'price']
