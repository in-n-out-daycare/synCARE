from django.shortcuts import render, redirect
from .models import Child, Activity, Guardian, Classroom, Visit
from django.views import generic
from django.db.models import Prefetch
import datetime


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
    is_guardian = request.user.groups.filter(name='guardian').exists()
    children = ()

    if is_administrator:
        children = Child.objects.all()

    if is_caregiver:
        
        children = Child.objects.filter(classroom__caregiver=request.user).prefetch_related(
                Prefetch(
                    "visits",
                    queryset=Visit.objects.filter(check_out__isnull=True),
                    to_attr="visit"
                )
            )

    if is_guardian:
        children = Guardian.objects.get(user=request.user).children.all
        return render(request, 'visit.html')

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

def nap(request):
    return render(request,'index.html', context=context)

def visit(request):
    return

def check_out(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    visit.check_out = datetime.datetime.now()
    visit.save()
    return redirect('index')

def check_in(request, child_id):
    child = Child.objects.get(child_id=child_id)
    visit = Visit(
        child=child
    )
    visit.save()
    return redirect('index')

