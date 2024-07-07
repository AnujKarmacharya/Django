from django.shortcuts import render, HttpResponse, redirect
from .models import Tasks

# Create your views here.


def index(request):
    # people = [{"name": "Ram", "age": 25}, {"name": "shyam", "age": 20}]

    tasks = Tasks.objects.all()
    context = {"tasks": tasks}

    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")


def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Tasks.objects.create(name=name, description=description)
        return redirect("/")
    return render(request, "create.html")


def mark_as_done(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.status = True
    task.save()
    return redirect("/")


def delete_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    return redirect("/")


def edit(request, pk):
    task = Tasks.objects.get(pk=pk)
    if request.method == "POST":
        task.name = request.POST.get("name")
        task.description = request.POST.get("description")
        task.save()
        return redirect("/") 
    context = {"task": task}
    return render(request, "edit.html", context)
