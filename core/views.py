from django.shortcuts import render
from .models import Child, Activity
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
    return render(request, 'index.html')
