from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
# Create your views here.

def index(request):
    t = get_template('base.html')
    html = t.render(Context({'name': 'JunYen'}))
    return HttpResponse(html)

def log_in(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
            return HttpResponseRedirect('/accounts/invalid')

def logged_in(request):
    return render_to_response('loggedin.html', { 'full_name' : request.user.username })

def invalid_login(request):
    return render_to_response('invalid.login.html')

def log_out(request):
    logout(request)
    return render_to_response('logout.html')
