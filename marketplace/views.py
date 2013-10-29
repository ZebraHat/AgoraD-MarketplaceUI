#-------------------------------------------------------------------------------
# Name:        views
# Purpose:     shows the website
# Usage:       through django webserver
#
# Author:      Lumate, LLC
#
# Created:     10/25/2013
# Copyright:   (c) Lumate, LLC
# Licence:     Public/Private
#-------------------------------------------------------------------------------

#Django Imports
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render


#Interface Imports
from models import *


def index(request):
    """ one-pager landing """
    return render(request, 'index.html')
    

@login_required()
def home(request):
    """ dashboard interface """
    return render(request, 'home.html')
