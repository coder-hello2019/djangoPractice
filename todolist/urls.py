from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('test1', views.test1, name='test'),
    path('list', views.showList, name='showList'),
    path('timer', views.timer, name='timer'),
    path('reqtest', views.reqTest, name='reqTest'),
    path('processRequest', views.processRequest, name='processRequest'),
    path('save', views.save, name='save')
]
