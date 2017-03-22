#coding=utf-8
from django.db import models

# Create your models here.
class Owner(models.Model):
	name = models.CharField(max_length=20)
	um  = models.CharField(max_length=30,null=True)
	role = models.CharField(max_length=4)

	def __unicode__(self):
		return self.name

class Project(models.Model):
	projectName  = models.CharField(max_length=20)
	owner = models.ForeignKey(Owner)

	def __unicode__(self):
		return self.name

class Case(models.Model):
	summary = models.CharField(max_length=100)
	details = models.TextField(max_length=255,null=True)
	owner =  models.ForeignKey(Owner,on_delete=models.CASCADE)
	createtime = models.DateField(auto_now_add=True)
	lastUpdateTime = models.DateField()
	# project = models.ForeignKey(Project,on_delete=models.CASCADE)


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



