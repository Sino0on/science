from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'science',
                  'profession', 'photo', 'phone',
                  'city', 'twitter', 'facebook',
                  'youtube']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class MaterialListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    disciplines = DisciplineSerializer(many=True)

    class Meta:
        model = Material
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    my_projects = ProjectSerializer(source='projects', many=True)
    my_materials = ProjectSerializer(source='materials', many=True)

    class Meta:
        model = Author
        fields = '__all__'


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class MaterialListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    disciplines = DisciplineSerializer(many=True)

    class Meta:
        model = Material
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    materials = MaterialListSerializer(source='materials')

    class Meta:
        model = Project
        fields = '__all__'
