from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Loginform, Loginform2, ProfileModel
from .models import ModelName


# Create your views here
def home(request):
    # if request.method == 'POST':
    #     form = FormName(request.POST)
    #     print(form)
    #     content = {
    #        'form':form
    #     }
    #     return render(request, "frontend/pages/home/home.html",content)
    # else:
    return render(request, "frontend/pages/home/home.html")


def index(request):
    return render(request, "frontend/pages/index/index.html")


def about(request):
    employee = ModelName.objects.all().count()
    context = {
        'employee': employee
    }
    return render(request, "frontend/pages/about/about.html", context)


def contact(request):
    # model form ko use garda last easy hunxa

    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        obj = ModelName.objects.create(first_name=first_name, last_name=last_name, email=email)
        if obj:
            return redirect('/contact')
        return HttpResponse("data is not created")
    else:
        data1 = ModelName.objects.all()
        context = {
            'form': data1
        }

        return render(request, "frontend/pages/contact/contact.html", context)


@login_required
def updates(request, id):
    f = ModelName.objects.get(id=id)
    if request.method == 'POST':
        f.first_name = request.POST['first_name']
        f.last_name = request.POST['last_name']
        f.email = request.POST['email']
        f.save()
        return redirect('/contact')
    context = {
        'f': f
    }

    print(id)
    return render(request, "frontend/pages/updates/updates.html", context)


def delete(request, id):
    f = ModelName.objects.get(id=id)
    if request.method == 'POST':
        f.delete()
        return redirect('/contact')
    context = {
        'f': f
    }

    return render(request, "frontend/pages/delete/delete.html", context)


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             data = form.cleaned_data
#             user = User.objects.create(username=data['username'], password=data['password1'])
#             user.save()
#             return redirect('/')
#     form = UserCreationForm()
#     context = {
#         'form': form
#     }
#     return render(request, "frontend/pages/register/register.html", context)


def register(request):
    # form = FormName2()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username'])
            user.set_password(data['password1'])
            user.save()
            # print(user.username)
            return redirect("/home")
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, "frontend/pages/register/register.html", context)


def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if User is not None:
                dj_login(request, user)
                return redirect('/')
            print(data)

    form = Loginform
    context = {
        'form': form
    }
    return render(request, "frontend/pages/login/login.html", context)


def logout(request):
    dj_logout(request)
    return redirect('/login')


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form=ProfileModel(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()

        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        obj = User.objects.get(id=request.user.id)
        obj.first_name = first_name
        obj.last_name = last_name
        obj.save()
        return redirect('/profile')
    form = Loginform2(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name})
    context = {
        'form': form,
        'profile_form': ProfileModel
    }
    return render(request, "frontend/pages/profile/profile.html", context)

