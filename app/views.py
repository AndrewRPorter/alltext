import os

from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader

from tools import format, db_interface

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")
    csrf_token = get_token(request)

    template_values = {
        "old_text": "",
        "formatted_text": "",
        "formats": format.get_formats(),
        "csrf_token": csrf_token,
    }

    if request.POST.get("type", "") == "format":
        db = os.path.join(BASE_DIR, "db.sqlite3")
        text = request.POST["old_text"]
        option = request.POST["selected"]
        template_values["old_text"] = text
        template_values["formatted_text"] = format.format(text, option=option)

        db_interface.commit(db, text)  # add formatted text to database



    return HttpResponse(template.render(template_values))
