from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('register/', register, name='register'),
    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('materials/', MaterialsListView.as_view(), name='materials'),
    path('cabinet/<int:pk>', PersonDetailView.as_view(), name='cabinet_detail'),
    path('material/<int:pk>', MaterialDetailView.as_view(), name='material_detail'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/update/<int:pk>', ProjectUpdateView.as_view(), name='project_update'),
    path('material/update/<int:pk>', MaterialUpdateView.as_view(), name='material_update'),
    path('person/update/<int:pk>', PersonUpdateView.as_view(), name='person_update'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('material/create/', MaterialCreateView.as_view(), name='material_create'),
    path('chat/<int:pk>', chat, name='chat'),
    path('resetPassword/', PasswordsChangeView.as_view(), name='resetPassword'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword2.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name='reset_password_complete'),
]