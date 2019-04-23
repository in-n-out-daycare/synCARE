import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db.models import Prefetch
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.views.decorators.http import require_http_methods
from .models import Child, Activity, Guardian, Classroom, Visit
from .forms import CommentForm


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


def action_summary(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    comment = visit.comment
    naps = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.NAP)
    outputs = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.OUTPUT)
    inputs = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.INPUT)
    child = visit.child
    guardians = child.guardians.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            if visit.comment == None:
                visit.comment = " - " + form.cleaned_data['comment']
            else:
                visit.comment += "\n - " + (form.cleaned_data['comment'])
            visit.save()

        return redirect('action_summary', visit_id=visit_id)

    else:
        form = CommentForm()

    context = {
        'form': form,
        'guardians': guardians,
        'naps': naps,
        'visit': visit,
        'child': child,
        'visit_id': visit_id,
        'outputs': outputs,
        'inputs': inputs,
        'comment': comment,
    }

    return render(request, 'action_summary.html', context=context)


def action_summary_email(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    naps = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.NAP)
    outputs = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.OUTPUT)
    child = visit.child
    guardians = child.guardians.all()
    inputs = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.INPUT)
    comment = visit.comment

    subject="Input//Output Daily Summary"
    to = [guardian.user.email for guardian in guardians]
    from_email = 'input_output@io.com'

    context = {
    'naps': naps,
    'visit': visit,
    'child': child,
    'visit_id': visit_id,
    'outputs': outputs,
    'inputs': inputs,
    'comment': comment,
    } 

    message=get_template('action_summary_email.html').render(context)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return redirect('index')


def in_list(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    context = {
        'visit_id' : visit_id
        }
    return render(request, 'in_list.html', context=context)


@require_http_methods(['POST'])
def bottle(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    option = request.POST['bottle_choice']
    bottle = Activity(
        activity_type=Activity.INPUT,
        subtype='bottle',
        subtype_option=option,
        visit=visit,
        child=visit.child,
    )
    bottle.save()
   
    return redirect('index')




@require_http_methods(['POST'])
def diaper(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    option = request.POST['diaper_choice']
    diaper = Activity(
        activity_type=Activity.OUTPUT,
        subtype='diaper',
        subtype_option=option,
        visit=visit,
        child=visit.child,
    )
    diaper.save()
   
    return redirect('index')

# def diaper_1(request, visit_id):
#     visit = get_object_or_404(Visit, id=visit_id)
#     diaper = Activity(
#         activity_type=Activity.OUTPUT,
#         subtype='1',
#         visit=visit,
#         child=visit.child
#     )
#     diaper.save()

#     return redirect('index')


# def diaper_2(request, visit_id):
#     visit = get_object_or_404(Visit, id=visit_id)
#     diaper = Activity(
#         activity_type=Activity.OUTPUT,
#         subtype='2',
#         visit=visit,
#         child=visit.child,
#     )
#     diaper.save()

#     return redirect('index')

@require_http_methods(['POST'])
def nurse(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    option = request.POST['nurse_choice']
    nurse = Activity(
        activity_type=Activity.INPUT,
        subtype='nursing',
        subtype_option=option,
        visit=visit,
        child=visit.child
    )
    nurse.save()

    return redirect('index')


@require_http_methods(['POST'])
def food(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    option = request.POST['food_choice']
    food = Activity(
        activity_type=Activity.INPUT,
        subtype='food',
        subtype_option=option,
        visit=visit,
        child=visit.child
    )
    food.save()

    return redirect('index')


def check_out(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    visit.check_out = datetime.datetime.now()
    naps = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.NAP)
    outputs = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.OUTPUT)
    child = visit.child
    guardians = child.guardians.all()
    inputs = Activity.objects.filter(visit_id=visit_id, activity_type=Activity.INPUT)
    comment = visit.comment

    subject="Input//Output Daily Summary"
    to = [guardian.user.email for guardian in guardians]
    from_email = 'input_output@io.com'

    context = {
    'naps': naps,
    'visit': visit,
    'child': child,
    'visit_id': visit_id,
    'outputs': outputs,
    'inputs': inputs,
    'comment': comment,
    } 

    message=get_template('action_summary_email.html').render(context)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
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
