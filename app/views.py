import os

from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader

from tools import format

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")
    csrf_token = get_token(request)

    template_values = {"formatted_text": "",
                       "formats": format.get_formats(),
                       "csrf_token": csrf_token}

    if request.POST.get("type", "") == "format":
        text = request.POST["text"]
        option = request.POST["selected"]
        template_values["formatted_text"] = format.format(text, option=option)

    return HttpResponse(template.render(template_values))
