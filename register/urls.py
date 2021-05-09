from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('loggedin', views.hello, name='loggedin')
]
