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
from django.template import RequestContext, loader


#Interface Imports
from models import *


def index(request):
    """ one-pager landing """
    return render(request, 'index.html')
    

@login_required()
def home(request):
    """ dashboard interface """

    # Get all the info that'll be displayed on the dashboard here
    # all Sellables with Seller=current user
    # all Transfers with Seller=current user or Buyer=current user

    # If we are a buyer AND there are no transfers above found, redirect to /listings

    return render(request, 'home.html')

@login_required()
def listings(request):
	""" data listings """

	template = loader.get_template('listings.html')
	context = RequestContext(request, {
		'test': [1, 2, 3, 4, 5, 6],
		'listings': Sellable.objects.all()
	})

	return HttpResponse(template.render(context))

@login_required()
def sell(request):
	""" list data for sale """

	return render(request, 'sell.html')

@login_required()
def transfers(request):
	""" data transfer log """

	return render(request, 'transfers.html')