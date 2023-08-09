from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from server.models import *
from django.views import generic
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class ProjectsListView(generic.ListView):
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'projects.html'
    paginate_by = 10


class MaterialsListView(generic.ListView):
    queryset = Project.objects.all()
    context_object_name = 'materials'
    template_name = 'materials.html'
    paginate_by = 10


class ProjectCreateView(generic.CreateView):
    model = Project
    template_name = 'project_create.html'
    context_object_name = 'form'
    form_class = ProjectForm


class MaterialCreateView(generic.CreateView):
    model = Project
    template_name = 'material_create.html'
    context_object_name = 'form'
    form_class = MaterialForm


def register(request):
    print('kirdi')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        print(form.errors)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserRegisterForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def loginpage(request):
    if request.method == "POST":
        print('login')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print('valid')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            print(form.errors)
            messages.error(request, "Invalid email or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logoutpage(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect(reverse('home'))


class PersonDetailView(generic.DetailView):
    template_name = 'cabinet.html'
    context_object_name = 'person'
    model = Person


class MaterialDetailView(generic.DetailView):
    template_name = 'material_detail.html'
    context_object_name = 'material'
    model = Material


class ProjectDetailView(generic.DetailView):
    template_name = 'project_detail.html'
    context_object_name = 'project'
    model = Project


class ProjectUpdateView(generic.UpdateView):
    template_name = 'project_update.html'
    context_object_name = 'form'
    model = Project
    form_class = ProjectForm


class MaterialUpdateView(generic.UpdateView):
    template_name = 'material_update.html'
    context_object_name = 'form'
    model = Material
    form_class = MaterialForm


class PersonUpdateView(generic.UpdateView):
    template_name = 'person_update.html'
    context_object_name = 'form'
    model = Person
    form_class = PersonUpdateForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'resetPassword.html'


def home(request):
    return redirect(reverse('projects'))
    # return render(request, 'index.html')


def chat(request, pk):
    return render(request, 'chat.html')
