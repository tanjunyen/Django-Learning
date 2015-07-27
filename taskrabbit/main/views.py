from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def index(request):
    t = get_template('base.html')
    html = t.render(Context({'name': 'JunYen'}))
    return HttpResponse(html)