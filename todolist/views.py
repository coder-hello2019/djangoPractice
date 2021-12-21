from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

from todolist.models import todoList

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# delete if not needed
from django.core import serializers

from datetime import timedelta
from datetime import timezone
import datetime
import json

from .helpers import *

# Create your views here.
def index(request):
    availableProjects = set([item.associatedProject for item in todoList.objects.all() if item.userID == request.user])

    return render(request, 'timer.html', context={'availableProjects': availableProjects})
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
        processedTimes = processTime(finishedTimers[itemi][0])
        hours, minutes, seconds = processedTimes['hours'], processedTimes['minutes'], processedTimes['seconds']
        newTodo = todoList(item = itemi, userID=request.user, duration = timedelta(hours=hours, minutes=minutes, seconds=seconds), associatedProject=finishedTimers[itemi][1])
        newTodo.save()

    # if request.method == 'POST':
    #     newTask = request.POST['completedTasks']
    return HttpResponse("Save has been called")

@login_required
def viewEntries(request):

    # fetch all user data to display, with the default of all time for the timespan
    allEntriesList, allProjectsDict, mostCommonEntries = fetchAllUserData(request, timespan = 'allTime')

    return render(request, 'viewEntries.html', context={'allEntries': allEntriesList, 'allProjectsDict': allProjectsDict, 'mostCommonEntries': mostCommonEntries})

@csrf_exempt
def deleteEntry(request):

    # delete corresponding entry from the model/database
    entryToDelete = todoList.objects.get(id = request.POST.get('entryID'))
    entryToDelete.delete()

    return HttpResponse(200)
    #return render(request, 'viewEntries.html', context={'allEntries': allEntriesList, 'allProjectsDict': allProjectsDict, 'mostCommonEntries': mostCommonEntries})


@csrf_exempt
def updateDiagrams(request):

    timespan = request.POST.get('timespan')
    """
    if timespan == 'allTime':
        return HttpResponse("All time works fine")
    elif timespan == 'thisMonth':
        return HttpResponse("This month works fine")
    else:
        return HttpResponse("Nothing bloody works")
    """
    allEntriesList, allProjectsDict, mostCommonEntries = fetchAllUserData(request, timespan)

    # allEntriesList = list of todolist objects - THIS IS THE BIT THAT IS CAUSING PROBLEMS
    # allProjectsDict = dict of strings and ints
    # mostCommonEntries = dict of strings and ints

    #returnData = {'allEntriesList': serializers.serializer(allEntriesList), 'allProjectsDict': allProjectsDict, 'mostCommonEntries': mostCommonEntries}
    returnData = {'allEntriesList': serializers.serialize("json", allEntriesList), 'allProjectsDict': allProjectsDict, 'mostCommonEntries': mostCommonEntries}
    print(type(allEntriesList))
    # this refreshes the page - ideally we would do this in place without a refresh

    return JsonResponse(returnData)

    #return HttpResponse(timespan)
    #return render(request, 'viewEntries.html', context={'allEntries': allEntriesList, 'allProjectsDict': allProjectsDict, 'mostCommonEntries': mostCommonEntries})


# THESE ARE NOT VIEWS - JUST HELPER FUNCTIONS. MOVE THEM TO HELPERS.PY FILE
def fetchAllUserData(request, timespan):
    today = datetime.date.today()

    # ALL USER DATA
    # fetch user data for just this month
    if timespan == 'thisMonth':
    #if timespan != 'allTime':
        allUserData = todoList.objects.all().filter(userID_id=request.user, entryTime__month = today.month)
    # or fetch data for all time, depending on user selection
    elif timespan == 'allTime':
        allUserData = todoList.objects.all().filter(userID_id=request.user)
    # or fetch data for just the current week (being the last 7 days, not the calendar week)
    else:
        today = datetime.datetime.now().date()
        thisTimeLastWeek = today - timedelta(days=7)
        tomorrow = today + timedelta(days=1)
        # we need to include tomorrow instead of today in the timerange because __range doesn't show the results for today (as per documentation)
        allUserData = todoList.objects.all().filter(entryTime__range=(thisTimeLastWeek, tomorrow))

    for item in allUserData:
        print(f"Relevant ID in allUserData: {item.id}")

    # convert the allUserData queryset into a list
    allUserEntries = [item for item in allUserData]

    # PROJECTS DATA
    # create ist of all (distinct) projects available for this user
    allProjects = allUserData.order_by().values_list('associatedProject').distinct()

    # turn projects data into a dictionary
    allProjectsDict = {item[0]: 0 for item in allProjects}

    totalSeconds = 0
    # record the total amount of time spent on each project
    for item in allUserData:
        # record how much time in seconds was spent on each project
        allProjectsDict[item.associatedProject] += item.duration.seconds
        totalSeconds += item.duration.seconds

    # MOST FREQUENTLY USED WORDS/DESCRIPTIONS
    # list of all time entry texts/descriptions (we don't want these to be distinct because we're collecting these items to then calculate the frequency of words used)
    # flat=True ensures that we get a list of strings rather than tuples
    allDescriptions = allUserData.order_by().values_list('item', flat=True)

    # find the most frequently used words
    mostCommonEntries = findMostCommonWords(allDescriptions)

    return (allUserData, allProjectsDict, mostCommonEntries)
