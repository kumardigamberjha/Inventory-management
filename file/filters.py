import django_filters

from .models import Issued_to, User_Master

class UserFilters(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = User_Master
        fields = ["first_name"]


class IssuedToFilters(django_filters.FilterSet):
    asset_id = django_filters.CharFilter(lookup_expr='iexact')
    # Users = django_filters.CharFilter()

    class Meta:
        model = Issued_to
        fields = ["asset_id", "Users","O_stock"]

# class IssuedToFilterss(django_filters.FilterSet):
#     asset_id = django_filters.CharFilter(lookup_expr='iexact')
    
#     class meta:
#         model = Issued_to
#         fields = "__all__"