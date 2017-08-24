
from ballerapp.forms import(
           UserForm,
           UserProfileForm,
           AddNewPlace,
           UserLoginForm
        )

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model





def index(request):
   return render_to_response('ballerapp/base.html')


def login_view(request):
    print(request.user.is_authenticated())
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated())
            return redirect('/ballerweb/home/')
    return render(request, "ballerapp/login.html", {"form":form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/ballerweb/home')


def add_new_place(request):
    if request.POST:
        form = AddNewPlace(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ballerweb/home')
    else:
        form = AddNewPlace()
    args = {}
    args['form'] = form
    return render(request , 'ballerapp/create_new_place.html', args, {'form': form})


def register_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save( commit=False)
            profile.user = user
            if 'picture' in request.FILES :
                profile.picture = request.FILES[ 'picture' ]
            registered = True
        else:
            print( user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'ballerapp/register.html',{ 'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    )
