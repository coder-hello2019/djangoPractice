from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registrationForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/register/loggedin')
        else:
            form = registrationForm()
            return render(request, 'register.html', context={'form': form})
    elif request.method == 'POST':
        # populate form with data from the request
        form = registrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            newUser = User.objects.create_user(username, email, password)
            newUser.save()
            return HttpResponse(f"{username} has been added to database")
        else:
            return HttpResponse(f'Form not valid: {form.errors}')
            #return render(request, 'redirected.html', context={'username': form})

def hello(request):
    return HttpResponse("Successfully logged in!")
