from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from todolist.models import todoList

from django.contrib.auth.models import User

import json

# Create your views here.
def index(request):
    return render(request, 'timer.html')
    #return HttpResponse("Hello Django!")

def test1(request):
    tasks = todoList.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

def showList(request):
    todos = todoList.objects.all()
    output = ''.join([todo.item for todo in todos])
    return HttpResponse(output)

def timer(request):
    return render(request, 'timer.html')

def reqTest(request):
    return render(request, 'reqTest.html')

@csrf_exempt
def processRequest(request):
    if request.method == 'POST':
        newTodo = todoList(item=request.POST['test'])
        newTodo.save()
    return HttpResponse("Request has been processed :)")

@csrf_exempt
def save(request):
    finishedTimers = json.loads(request.POST['completedTasks'])
    for itemi in finishedTimers:
        newTodo = todoList(item = itemi)
        newTodo.save()

    # if request.method == 'POST':
    #     newTask = request.POST['completedTasks']
    return HttpResponse("Save has been called")
