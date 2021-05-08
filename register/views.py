from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registrationForm

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = registrationForm()
        return render(request, 'register.html', context={'form': form})
    elif request.method == 'POST':
        # populate form with data from the request
        form = registrationForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['password1'])
        else:
            return HttpResponse('Form not valid')
            #return render(request, 'redirected.html', context={'username': form})
