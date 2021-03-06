
from ballerapp.forms import(
           UserForm,
           AddNewPlace,
           UserLoginForm
        )
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ballerapp.models import Adresse
from django.views.generic.list import ListView



"""def index(request):
    user = "%s" %(request.user)
    adresse = Adresse.objects.all()
    context={
        "username": user,
        "adresse": adresse,
    }
    return render(request, "ballerapp/base.html", context)
"""
class AdresseListView(ListView):

    model = Adresse

    #template_name = "ballerapp/base.html"
    def get_context_data(self, **kwargs):
        context = super(AdresseListView, self).get_context_data(**kwargs)
        context['adresse']= Adresse.objects.all()
        img = Adresse.place_pic

        return context


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
    return render(request, 'ballerapp/login.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/ballerweb/home')


def add_new_place(request):

    if request.method == 'POST':
        form = AddNewPlace(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ballerweb/home')
    else:
        form = AddNewPlace()
    args = {}
    args['form'] = form
    return render(request, 'ballerapp/create_new_place.html', args, {'form': form})


def register_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid(): # and profile_form.is_valid()
            user = user_form.save()
            user.set_password(user.password)
            user.save()
           # profile = profile_form.save( commit=False)
           # profile.user = user
            #if 'picture' in request.FILES :
             #   profile.picture = request.FILES[ 'picture' ]
            registered = True
            login(request, user)
        else:
            print(user_form.errors)# , profile_form.errors
    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()
    return render(request, 'ballerapp/register.html', {'user_form': user_form, 'registered': registered} # 'profile_form': profile_form,
    )
