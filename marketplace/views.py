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
from itertools import chain
from django.shortcuts import get_object_or_404


#Interface Imports
from models import *


def index(request):
    """ one-pager landing """
    return home(request)
    #return render(request, 'index.html')
    

#@login_required()
def home(request):
    """ dashboard interface """

    current_user = request.user

    bought_transfers = Transfer.objects.all()#.filter(buyer=current_user) # temp
    sold_transfers = Transfer.objects.all()#.filter(seller=current_user) # temp
    all_transfers = sorted(
        chain(bought_transfers, sold_transfers),
        key=lambda instance: instance.transaction_queued
    )

    template = loader.get_template('home.html')
    context = RequestContext(request, {
        'list_count': len(Sellable.objects.all()), # probably hilariously optimizable
        'sell_data': '0GB', #todo calculate this
        'transfer_count': len(all_transfers)
    })

    return HttpResponse(template.render(context))

#@login_required()
def listings(request):
    """ data listings """

    template = loader.get_template('listings.html')
    context = RequestContext(request, {
        'listings': Sellable.objects.all()
    })

    return HttpResponse(template.render(context))

#@login_required()
def sell(request):
    """ list data for sale """

    # If we catch a POST request, process it
    if request.method == 'POST':
    	#TODO validation
    	sellable = Sellable.new(request.POST)
    	sellable.save

    return render(request, 'sell.html')

#@login_required()
def transfers(request):
    """ data transfer log """

    current_user = request.user

    bought_transfers = Transfer.objects.all()#.filter(buyer=current_user) # temp
    sold_transfers = Transfer.objects.all()#.filter(seller=current_user) # temp
    all_transfers = sorted(
        chain(bought_transfers, sold_transfers),
        key=lambda instance: instance.transaction_queued
    )

    template = loader.get_template('transfers.html')
    context = RequestContext(request, {
        'transfer_list': all_transfers,
        'bought_transfers': bought_transfers,
        'sold_transfers': sold_transfers
    })

    return HttpResponse(template.render(context))

#@login_required()
def detail(request, listing_id):
	""" listing detail page """

	listing = Sellable.objects.filter(id=listing_id)
	#listing = get_object_or_404(Sellable, id=listing_id) # temp disabled

	template = loader.get_template('detail.html')
	context = RequestContext(request, {
		'listing': listing
	})

	return HttpResponse(template.render(context))