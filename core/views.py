from django.shortcuts import render
from .models import Child, Activity, Guardian, Classroom
from django.views import generic


# Create your views here.
# def index(request):
    
#     all_children = Child.objects.all()

#     context = {
#         'all_children': all_children
#     }

#     return render(request, 'index.html', context=context)

# class-based view, if wanting to try
# class Index(generic.ListView):
#     model = Child


class ActivityListView(generic.ListView):
    model = Activity

# Create your views here.
def index(request):

    is_administrator = request.user.groups.filter(name='administrator').exists()
    is_caregiver = request.user.groups.filter(name='caregiver').exists()
    is_guardian = request.user.groups.filter(name='guardian').exists()added 
    children = ()

    if is_administrator:
        children = Child.objects.all()

    if is_caregiver:
        children = Child.objects.filter(classroom__caregiver=request.user)

    if is_guardian:
        children = Guardian.objects.get(user=request.user).children.all

    context = {
        'children': children,
        'isguardian': is_guardian,
        'iscaregiver': is_caregiver,
        'isadministrator': is_administrator,
    }
    return render(request, 'index.html', context=context)

def food(request):
    return render(request, 'food.html')

def diaper(request):
    return render(request, 'diaper.html')