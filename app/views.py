from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    template_values = {}
    
    return HttpResponse(template.render(template_values))
