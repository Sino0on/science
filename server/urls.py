from django.urls import path
from .views import *


urlpatterns = [
    path('auth/register', PersonCreateView.as_view()),
    path('auth/login', NewAuthView.as_view()),
    path('auth/verify/', TokenVerifyCustomView.as_view()),
    path('city/create', CityCreateView.as_view()),
    path('city/list', CityListView.as_view()),
    path('city/<int:pk>', CityDetailView.as_view()),
    path('project/create', ProjectCreateView.as_view()),
    path('project/list', ProjectListView.as_view()),
    path('project/<int:pk>', ProjectDetailView.as_view()),
    path('project/detail/<int:pk>', ProjectDetail2View.as_view()),
    path('profession/create', ProfessionCreateView.as_view()),
    path('profession/list', ProfessionListView.as_view()),
    path('profession/<int:pk>', ProfessionDetailView.as_view()),
    path('science/create', ScienceCreateView.as_view()),
    path('science/list', ScienceListView.as_view()),
    path('science/<int:pk>', ScienceDetailView.as_view()),
    path('material/create', MaterialCreateView.as_view()),
    path('material/list', MaterialListView.as_view()),
    path('material/<int:pk>', MaterialDetailView.as_view()),
    path('author/<int:pk>', AuthorDetailView.as_view()),
    path('material/detail/<int:pk>', MaterialDetail2View.as_view()),
    path('person/list', PersonListView.as_view()),
    path('person/<int:pk>', PersonDetailView.as_view()),
    path('authors/list', AuthorListView.as_view()),
    path('chat/list', ChatListView.as_view()),
    path('country/create', CountryCreateView.as_view()),
    path('country/list', CountryListView.as_view()),
    path('country/<int:pk>', CountryDetailView.as_view()),
    path('chat/<int:pk>', ChatDetailView.as_view()),
    path('find/chat/<int:id>', ChatFinder.as_view()),
]
