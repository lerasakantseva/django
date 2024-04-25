from backend.models import Core, Boost
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from .forms import UserForm
from .serializers import UserSerializer, UserSerializerDetail
from backend.serializers import BoostSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerDetail


class BoostViewSet(viewsets.ModelViewSet):
    queryset = Boost.objects.all()
    serializer_class = BoostSerializer

    def get_queryset(self):
        core = Core.objects.get(user=self.request.user)
        boosts = Boost.objects.filter(core=core)
        return boosts


def index(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) != 0:
        core = Core.objects.get(user=request.user)
        return render(request, 'index.html', {'core': core})
    else:
        return redirect('login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'invalid': True})
    else:
        return render(request, 'login.html', {'invalid': False})

def user_logout(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == 'POST':
        print(111111111111)
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            existing_user = User.objects.filter(username=username)
            if len(existing_user) == 0:
                password = form.cleaned_data['password']
                user = User.objects.create_user(username, '', password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                core = Core(user=user)
                core.save()
                return redirect('index')
            else:
                return render(request, 'registration.html', {'invalid': True, 'form': form})
        else:
            return render(request, 'registration.html', {'invalid': False, 'form': form})

    if request.method == 'GET':
        form = UserForm()
        return render(request, 'registration.html', {'invalid': False, 'form': form})