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
    path('profession/create', ProfessionCreateView.as_view()),
    path('profession/list', ProfessionListView.as_view()),
    path('profession/<int:pk>', ProfessionDetailView.as_view()),
    path('science/create', ScienceCreateView.as_view()),
    path('science/list', ScienceListView.as_view()),
    path('science/<int:pk>', ScienceDetailView.as_view()),
    path('materail/create', MaterialCreateView.as_view()),
    path('materail/list', MaterialListView.as_view()),
    path('materail/<int:pk>', DisciplineDetailView.as_view()),
    path('discipline/create', DisciplineCreateView.as_view()),
    path('discipline/list', DisciplineListView.as_view()),
    path('discipline/<int:pk>', DisciplineDetailView.as_view()),
]