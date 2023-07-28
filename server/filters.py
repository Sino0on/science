import django_filters
from .models import *


class MaterialFilter(django_filters.FilterSet):
    class Meta:
        model = Material
        fields = ['disciplines', 'title']


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['disciplines', 'title']
