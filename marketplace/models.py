#-------------------------------------------------------------------------------
# Name:        models
# Purpose:     defines models for the system
# Usage:       from models import *
#
# Author:      Lumate, LLC
#
# Created:     10/25/2013
# Copyright:   (c) Lumate, LLC
# Licence:     Public/Private
#-------------------------------------------------------------------------------


# Django imports
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django import forms

class Company(models.Model):
	# contains many Sellers
	name = models.CharField("company name", max_length=64)
	#logo = models.ImageField("company logo", blank=True)
	link = models.URLField("website link", blank=True)

	def __unicode__(self):
		return self.name

class User(models.Model):
	name     = models.CharField("real name", max_length=64, primary_key=True)
	email    = models.CharField("email address", max_length=128) # used as username to log in
	password = forms.PasswordInput()

	#class Meta:
	#	abstract = True

	def __unicode__(self):
		return self.name

class Buyer(User):
	user_id = models.ForeignKey(User, related_name='+')

class Seller(User):
	user_id = models.ForeignKey(User, related_name='+')
	company = models.ForeignKey(Company)

class Sellable(models.Model):
	CATEGORIES = ( # TBD; should sellers be able to add their own?
		('ANALYTICS', 'Analytics'),
		('INTERESTS', 'Interests'),
		('LOCATIONS', 'Locations')
	)

	# Metadata
	seller = models.ForeignKey(Seller)
	data_location = models.CharField("data location", max_length=64)
	creation_date = models.DateField("creation date")

	# List information
	title = models.CharField("listing title", max_length=256)
	description = models.CharField("listing description", max_length=1024) # probably make textfield instead
	for_sale_date = models.DateField("date to start selling") # allow sellers to put data for sale at a future date
	category = models.CharField("data category", max_length=1, choices=CATEGORIES)

	def data_size(self): # computes data size if json blob/text dump, does something else if url to database
		pass

	def save(self, *args, **kwargs):
		# Whenever a Sellable is modified, queue it up to save *after* any pending transfers of it are finished
		# todo
		super(Sellable, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Transfer(models.Model):
	seller = models.ForeignKey(Seller)
	buyer  = models.ForeignKey(User, related_name='+') # allow buyers and sellers to buy, but only sellers to sell
	data   = models.ForeignKey(Sellable)
	transaction_queued = models.DateField("transfer initiated")
	transaction_completed = models.DateField("transfer complete")

	def save(self, *args, **kwargs):
		# hit highway/dock to let them know a transfer is ready to be made

	    #:param token: API token for this loading dock
	    #:param table_names: A list of table names to transfer
	    #:param destination: The IP or host to transfer to
	    #:param session_id: ID of session from the MarketPlace
	    #:param database_name: Name of database to transfer
		#thing.com/highway/transfer/start/

		super(Transfer, self).save(*args, **kwargs)

	def __unicode__(self):
		return "transfer from " + self.seller + " to " + self.buyer