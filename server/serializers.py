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

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

    class Meta:
        model = Material
        fields = '__all__'


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    my_projects = ProjectSerializer(source='projects', many=True)
    my_materials = ProjectSerializer(source='materials', many=True)
    person = PersonListSerializer()

    class Meta:
        model = Author
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    pdf = serializers.FileField()
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
    project_materials = MaterialListSerializer(source='materials')

    class Meta:
        model = Project
        fields = '__all__'


class ChatFindSerializer(serializers.Serializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())

    class Meta:
        fields = ['members']


class MessageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        data = {
            "type": "chat_message",
            "result": representation
        }
        return data

    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, source='messages_chat')

    class Meta:
        model = Chat
        fields = '__all__'


class Chat2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
