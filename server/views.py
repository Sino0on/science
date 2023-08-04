from django.conf import settings
from rest_framework import generics, filters as fr, status
from .serializers import *
from django_filters import rest_framework as filters
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, UntypedToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .filters import ProjectFilter, MaterialFilter, PersonFilter, AuthorFilter
from .paginations import MyCustomPagination


class PersonCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = Person.objects.create(
                username=serializer.validated_data.get('username', None),
                first_name=serializer.validated_data.get('first_name', None),
                last_name=serializer.validated_data.get('last_name', None),
                email=serializer.validated_data.get('email', None),
                profession=serializer.validated_data.get('profession', None),
                science=serializer.validated_data.get('science', None),
                photo=serializer.validated_data.get('photo', None),
                phone=serializer.validated_data.get('phone', None),
                city=serializer.validated_data.get('city', None),
                twitter=serializer.validated_data.get('twitter', None),
                facebook=serializer.validated_data.get('facebook', None),
                youtube=serializer.validated_data.get('youtube', None),
            )
            user.set_password(serializer.validated_data['password'])
            try:
                validate_password(serializer.validated_data['password'], user)
            except ValidationError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            das = user.save()
            print(user.pk)
            author = Author.objects.create(person=user)
            token = TokenObtainPairSerializer()
            token = token.validate({'username': user.username, 'password': serializer.validated_data['password']})
            # print(token)
            token["user"] = PersonListSerializer(user).data
            # das = TokenObtainSerializer(data={
            #     'username': serializer.validated_data['username'],
            #     'password': serializer.validated_data['password']
            # })
            # if das.is_valid():
            #     print(das.validated_data)
            return Response(token, status=status.HTTP_200_OK)
        errors = serializer.errors
        print(errors)
        return Response(errors, status=status.HTTP_403_FORBIDDEN)


class NewAuthView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            user = Person.objects.get(username=request.data['username'])
            serializer.validated_data['user'] = PersonListSerializer(user).data

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TokenVerifyCustomSerializer(TokenVerifySerializer):
    def validate(self, attrs):
        token = UntypedToken(attrs["token"])

        if (
            api_settings.BLACKLIST_AFTER_ROTATION
            and "rest_framework_simplejwt.token_blacklist" in settings.INSTALLED_APPS
        ):
            jti = token.get(api_settings.JTI_CLAIM)
            if BlacklistedToken.objects.filter(token__jti=jti).exists():
                raise ValidationError("Token is blacklisted")

        return {"detail": "Токен действителен", "code": "token_valid"}


class TokenVerifyCustomView(TokenVerifyView):
    serializer_class = TokenVerifyCustomSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CityCreateView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)


class ProfessionCreateView(generics.CreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (IsAuthenticated,)


class MaterialCreateView(generics.CreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticated,)


class ScienceCreateView(generics.CreateAPIView):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    permission_classes = (IsAuthenticated,)


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend, fr.OrderingFilter)
    filterset_class = ProjectFilter
    # ordering_fields = ['price', 'likes']
    pagination_class = MyCustomPagination


class ProfessionListView(generics.ListAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class MaterialListView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialListSerializer
    filter_backends = (filters.DjangoFilterBackend, fr.OrderingFilter)
    filterset_class = MaterialFilter
    # ordering_fields = ['price', 'likes']
    pagination_class = MyCustomPagination


class ScienceListView(generics.ListAPIView):
    serializer_class = ScienceSerializer
    queryset = Science.objects.all()


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'pk'


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'


class ProfessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    lookup_field = 'pk'


class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    lookup_field = 'pk'


class MaterialDetail2View(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialListSerializer
    lookup_field = 'pk'


class ScienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    lookup_field = 'pk'


class DisciplineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    lookup_field = 'pk'


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CountrySerializer
    lookup_field = 'pk'


class DisciplineListView(generics.ListAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DisciplineCreateView(generics.CreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = (IsAuthenticated,)


class CountryCreateView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer
    lookup_field = 'pk'


class PersonListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer
    filter_backends = (filters.DjangoFilterBackend, fr.OrderingFilter)
    filterset_class = PersonFilter
    # ordering_fields = ['price', 'likes']
    pagination_class = MyCustomPagination


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (filters.DjangoFilterBackend, fr.OrderingFilter)
    filterset_class = AuthorFilter


class ProjectDetail2View(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    lookup_field = 'pk'
    serializer_class = ProjectListSerializer


class ChatFinder(generics.GenericAPIView):
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(request.user)
        user = request.user
        queryset = [user, Person.objects.get(id=self.lookup_field)]
        chat = Chat.object.get(members=queryset)
        if chat:
            chat_data = ChatSerializer(chat)
            chat_data.is_valid(raise_exception=True)
            return Response(data=chat_data.data, status=status.HTTP_200_OK)
        else:
            chat = Chat.objects.create(members=queryset)
            chat_data = ChatSerializer(chat)
            chat_data.is_valid(raise_exception=True)
            return Response(data=chat_data.data, status=status.HTTP_200_OK)

