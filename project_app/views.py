from django.shortcuts import render
from project_app.forms import UserForm, UserFileUploadForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo


# Create your views here.


def index(request):
    return render(request, 'project_app/index.html')


@login_required
def special(request):
    return HttpResponse("Has ingresado correctamente")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'project_app/registration.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse("Tu cuenta no eta activa o no existe")
        else:
            print("Ha fallado el ingreso a la cuenta")
            return HttpResponse("datos de ingreso invalidos")

    else:
        return render(request, 'project_app/login.html')


@login_required
def upload_files(request):


    if request.method == 'POST':
        form = UserFileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            print("guardado")
            return HttpResponseRedirect(reverse('index'))
    else:

        form = UserFileUploadForm()
        return render(request, 'project_app/file_upload.html', {'uploads': form})
