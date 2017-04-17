#coding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
# Create your models here.

# @python_2_unicode_compatible
class Owner(models.Model):
	name = models.CharField(max_length=20)
	um  = models.CharField(max_length=30,null=True)
	role = models.CharField(max_length=4)
	# def __str__(self):
	def __unicode__(self):
		return self.name

class Project(models.Model):
	projectName  = models.CharField(max_length=20)
	name = models.ForeignKey(Owner)
	# def __str__(self):
	def __unicode__(self):
		return self.projectName

class Interfaces(models.Model):
	interfName = models.CharField(max_length=30)
	interfDns = models.CharField(max_length=255)
	interfPath = models.CharField(max_length=50)
	interfMethod = models.CharField(max_length=4)
	interfParams = models.TextField(max_length=255)
	result = models.CharField(max_length=30,null=True,blank=True)
	createTime =  models.DateField(default=now)
	lastUpdateTime = models.DateField(default=now)
	projectName = models.ForeignKey(Project)
	header = models.CharField(max_length=100,null=True,blank=True)
	# name = models.ForeignKey(Owner)
	# dels = models.BooleanField(default=False)
	# def __str__(self):
	def __unicode__(self):
		return self.interfName

class Case(models.Model):
	summary = models.CharField(max_length=100)
	details = models.TextField(max_length=255,null=True)
	name =  models.ForeignKey(Owner)
	projectName = models.ForeignKey(Project)
	createTime =  models.DateField(default=now)
	lastUpdateTime = models.DateField(default=now)
	checkPoint = models.CharField(max_length=200,null=True,blank=True)
	interfName = models.ForeignKey(Interfaces)
	# def __str__(self):
	def __unicode__(self):
		return self.summary


