from django.db import models

# Create your models here.
class Owner(models.Model):
	name = models.CharField(max_length=20)
	um  = models.CharField(max_length=30,null=True)
	role = models.BooleanField()

class Project(models.Model):
	name  = models.CharField(max_length=20)
	dels = models.BooleanField()
	owner = models.ForeignKey(Owner)

class Case(models.Model):
	summary = models.CharField(max_length=100)
	details = models.CharField(max_length=255,null=True)
	owner =  models.ForeignKey(Owner)
	createtime = models.DateField(auto_now_add=True)
	lastUpdateTime = models.DateField()
	dels = models.BooleanField()


class Interfaces(models.Model):
	project = models.ForeignKey(Project)
	interfName = models.CharField(max_length=30)
	interfDns = models.CharField(max_length=30)
	interfPath = models.CharField(max_length=50)
	interfMethod = models.CharField(max_length=10)
	interfParams = models.CharField(max_length=255)
	excuteResult = models.CharField(max_length=30,null=True)
	createTime =  models.DateField(auto_now_add=True)
	lastUpdateTime = models.DateField()
	owner = models.ForeignKey(Owner)
	case = models.ForeignKey(Case)
	dels = models.BooleanField()



