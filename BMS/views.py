from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Account
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect('list/')
        else:
            return render(request, 'BMS/login.html', {})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('list/')
        else:
            return render(request, 'BMS/failed.html', {})

def homepage(request):
	return render(request,'BMS/home.html')

class UserList(ListView):
    model = Account

class Create(CreateView):
    model = Account
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = '/admin/'

class UserUpdate(UpdateView):
    model = Account
    success_url = '/admin/'
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name_suffix = '_update_form'

class Delete(DeleteView):
    model = Account
    success_url = '/admin/'
