from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.conf import settings
from djangotailoring.views import TailoredDocView
from djangotailoring.project import getsubjectloader
from mynav.nav import main_nav, tasks_nav
from .steps import steps_nav
from mylogger.models import ELog

# Create your views here.

@staff_member_required
def your_tail_view(request):
    headers = [f.name for f in ELog._meta.fields]
    tail = ELog.objects.filter(who=request.user).order_by('-mwhen').values_list()[0:20]
    return render(request, 'myusage/log_tail.html', {
        "main_nav": main_nav(request.user, 'staff_view'),
        "tasks_nav": tasks_nav(request.user, 'usage'),
        "steps_nav": steps_nav(request.user, 'your_tail'),
        "headers": headers,
        "tail": tail
    })

@staff_member_required
def everyone_tail_view(request):
    headers = [f.name for f in ELog._meta.fields]
    tail = ELog.objects.order_by('-mwhen').values_list()[0:20]
    return render(request, 'myusage/log_tail.html', {
        "main_nav": main_nav(request.user, 'staff_view'),
        "tasks_nav": tasks_nav(request.user, 'usage'),
        "steps_nav": steps_nav(request.user, 'eveyone_tail'),
        "headers": headers,
        "tail": tail
    })



