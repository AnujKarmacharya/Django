from django.shortcuts import render
from .models import Tasks

# Create your views here.


def index(request):
    # people = [{"name": "Ram", "age": 25}, {"name": "shyam", "age": 20}]

    tasks = Tasks.objects.all()
    context = {"tasks": tasks}

    return render(request, "index.html", context)
