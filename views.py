from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.conf import settings
from djangotailoring.views import TailoredDocView
from djangotailoring.project import getsubjectloader
from mynav.nav import main_nav, tasks_nav
from .steps import steps_nav

# Create your views here.

def by_user_view(request):
    return render(request, 'myusage/by_user.html', {
        "main_nav": main_nav(request.user, 'staff_view'),
        "tasks_nav": tasks_nav(request.user, 'publish'),
        "steps_nav": steps_nav(request.user, 'by_user')
    })


