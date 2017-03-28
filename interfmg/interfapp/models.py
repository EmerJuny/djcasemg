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
	ownerId = models.ForeignKey(Owner,on_delete=models.PROTECT,related_name='ownerId')
	ownerName  = models.CharField(max_length=20)
	def __unicode__(self):
		return self.projectName

class Case(models.Model):
	# id = models.IntegerField(primary_key=True)
	summary = models.CharField(max_length=100)
	details = models.TextField(max_length=255,null=True)
	owner =  models.CharField(max_length=10)
	project = models.CharField(max_length=60,null=True,blank=True)
	createTime =  models.DateField(default=now)
	lastUpdateTime = models.DateField(default=now)
	def __unicode__(self):
		return self.id


class Interfaces(models.Model):
	project = models.ForeignKey(Project)
	interfName = models.CharField(max_length=30)
	interfDns = models.CharField(max_length=30)
	interfPath = models.CharField(max_length=50)
	interfMethod = models.CharField(max_length=10)
	interfParams = models.TextField(max_length=255)
	excuteResult = models.CharField(max_length=30,null=True)
	createTime =  models.DateField(auto_now_add=True)
	lastUpdateTime = models.DateField()
	owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
	case = models.ForeignKey(Case,on_delete=models.CASCADE)
	dels = models.BooleanField(default=False)



