from django.urls import path

from . import views

app_name = 'engine'

urlpatterns = [
    path('', views.index, name='index'),
    path('addnewsource/', views.addnewsource, name='ans'),

]
