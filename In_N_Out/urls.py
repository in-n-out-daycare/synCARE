"""In_N_Out URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from core import views
from django.conf.urls.static import static
from django.conf import settings
import uuid

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('home/', views.index, name='index'),
    path('activity_list/<int:visit_id>/', views.action_list, name='action_list'),
    path('activity_list/<int:visit_id>/summary/', views.action_summary, name='action_summary'),
    path('activity_list/<int:visit_id>/summary/email/', views.action_summary_email, name='action_summary_email'),
    path('activity_list/in_list/<int:visit_id>/',views.in_list, name='in_list' ),
    path('activity_list/in_list/<int:visit_id>/bottle/', views.bottle, name='bottle'),
    # bottle moved from right after in_list to end of url to mirror nurse and food. potential trouble spot
    path('activity_list/in_list/<int:visit_id>/nurse/', views.nurse, name='nurse'),
    path('activity_list/diaper/<int:visit_id>/', views.diaper, name='diaper'),
    path('activity_list/diaper/<int:visit_id>/diaper_1/', views.diaper_1, name='diaper_1'),
    path('activity_list/diaper/<int:visit_id>/diaper_2/', views.diaper_2, name='diaper_2'),
    path('visit/', views.ActivityListView.as_view(), name='visit'),
    # allauth registration
    path('accounts/', include('allauth.urls')),
    path('visit/check_out/<int:visit_id>/', views.check_out, name='check_out'),
    path('visit/new/<uuid:child_id>/', views.check_in, name='check_in'),
    path('visit/nap_in/<int:visit_id>/', views.nap_in, name='nap_in'),
    path('visit/nap_out/<int:activity_id>/', views.nap_out, name='nap_out'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
