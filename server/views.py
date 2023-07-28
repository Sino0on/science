from django.shortcuts import render
from .models import Person
from django.conf import settings
from rest_framework import generics, status
from .serializers import *
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
from rest_framework.permissions import IsAdminUser


class PersonCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = Person.objects.create(
                username=serializer.validated_data['username'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                email=serializer.validated_data['email'],
                profession=serializer.validated_data['profession'],
                science=serializer.validated_data['science'],
            )
            user.set_password(serializer.validated_data['password'])
            try:
                validate_password(serializer.validated_data['password'], user)
            except ValidationError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            das = user.save()
            token = TokenObtainPairSerializer()
            token = token.validate({'username': user.username, 'password': serializer.validated_data['password']})
            # print(token)
            token["user"] = PersonSerializer(user).data
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
            serializer.validated_data['user'] = PersonSerializer(user).data

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
    serializer_class = CitySerializer
    permission_classes = (IsAdminUser,)


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminUser,)


class ProfessionCreateView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    permission_classes = (IsAdminUser,)


class MaterialCreateView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    permission_classes = (IsAdminUser,)


class ScienceCreateView(generics.CreateAPIView):
    serializer_class = ScienceSerializer
    permission_classes = (IsAdminUser,)


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer


class ProfessionListView(generics.ListAPIView):
    serializer_class = ProfessionSerializer


class MaterialListView(generics.ListAPIView):
    serializer_class = MaterialSerializer


class ScienceListView(generics.ListAPIView):
    serializer_class = ScienceSerializer


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    lookup_field = 'pk'


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    lookup_field = 'pk'


class ProfessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfessionSerializer
    lookup_field = 'pk'


class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializer
    lookup_field = 'pk'


class ScienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScienceSerializer
    lookup_field = 'pk'

