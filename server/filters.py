import django_filters
from .models import *


class MaterialFilter(django_filters.FilterSet):
    class Meta:
        model = Material
        fields = ['id', 'disciplines', 'title']


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['id', 'disciplines', 'title']


class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'middle_name']


class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'person']
