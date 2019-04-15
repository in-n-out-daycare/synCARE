from django.shortcuts import render
from .models import Child, Activity
from django.views import generic


# Create your views here.

class ChildListView(generic.ListView):
    model = Child;

class ActivityListView(generic.ListView):
    model = Activity;

def eat(request):
    