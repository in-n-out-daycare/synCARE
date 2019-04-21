import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db.models import Prefetch
from django.views.decorators.http import require_http_methods
from .models import Child, Activity, Guardian, Classroom, Visit


class ActivityListView(generic.ListView):
    model = Activity


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
                    queryset=Visit.objects.filter(check_out__isnull=True, check_in__date__lte=datetime.date.today()),
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

def action_list(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    activity = visit.activities
    nap = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.NAP, end_time__isnull=True)
    context = {
        'activity': activity,
        'visit': visit,
        'child': visit.child,
        'visit_id': visit_id,
        'open_nap':nap,
    }
    return render(request, 'action_list.html', context=context)

def in_list(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    context = {
        'visit_id' : visit_id
        }
    return render(request, 'in_list.html', context=context)


@require_http_methods(['POST'])
def bottle(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    option = request.POST['choice']
    bottle = Activity(
        activity_type=Activity.INPUT,
        subtype='bottle',
        subtype_option=option,
        visit=visit,
        child=visit.child,
    )
    bottle.save()
   
    return redirect('in_list', visit_id=visit_id)

def diaper(request):
    return 

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

def nap_out(request, activity_id):
    nap = Activity.objects.get(id=activity_id)
    nap.end_time = datetime.datetime.now()
    nap.save()
    return redirect('action_list', visit_id=nap.visit.id)

def nap_in(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    nap = Activity(
        activity_type=Activity.NAP,
        visit=visit,
        child=visit.child,
    )
    nap.save()
    
    return redirect('action_list', visit_id=visit_id)
