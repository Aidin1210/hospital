import django_filters
from api.models import Doctor

class DoctorFilterset(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')  # Поиск по имени, игнорируя регистр
    last_name = django_filters.CharFilter(lookup_expr='icontains')   # Поиск по фамилии, игнорируя регистр
    specialization = django_filters.CharFilter(lookup_expr='icontains')  # Поиск по специализации

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization']





# import django_filters as filters
#
# from api.models import Doctor
#
#
# class DoctorFilterset(filters.FilterSet):
#     last_name = filters.CharFilter(field_name='last_name',)
#
#     class Meta:
#         model = Doctor
#         fields = {'last_name':['exact', 'contain'],
#                   'first_name': ['exact'],
#                 'specialization': ['exact',]
#                   }




