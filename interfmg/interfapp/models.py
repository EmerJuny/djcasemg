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
	def __unicode__(self):
		return self.name

class Project(models.Model):
	projectName  = models.CharField(max_length=20)
	name = models.ForeignKey(Owner)
	def __unicode__(self):
		return self.projectName

class Case(models.Model):
	# id = models.IntegerField(primary_key=True)
	summary = models.CharField(max_length=100)
	details = models.TextField(max_length=255,null=True)
	name =  models.ForeignKey(Owner)
	projectName = models.ForeignKey(Project)
	createTime =  models.DateField(default=now)
	lastUpdateTime = models.DateField(default=now)
	def __unicode__(self):
		return self.summary


class Interfaces(models.Model):
	interfName = models.CharField(max_length=30)
	interfDns = models.CharField(max_length=30)
	interfPath = models.CharField(max_length=50)
	interfMethod = models.CharField(max_length=4)
	interfParams = models.TextField(max_length=255)
	excuteResult = models.CharField(max_length=30,null=True,blank=True)
	createTime =  models.DateField(default=now)
	lastUpdateTime = models.DateField(default=now)
	projectName = models.ForeignKey(Project)
	name = models.ForeignKey(Owner)
	summary = models.ForeignKey(Case)
	dels = models.BooleanField(default=False)
	def __unicode__(self):
		return self.interfName



