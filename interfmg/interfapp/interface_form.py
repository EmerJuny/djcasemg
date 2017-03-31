# coding=utf-8
from django import forms
from interfapp.models import Interfaces,Case,Owner,Project
from django.forms import ModelForm,Textarea
from django.utils.translation import ugettext_lazy as _
class InterfaceForm(forms.Form):
    METHOD_TYPE=(('POST','POST'),('GET','GET'),)
    projectName = forms.ModelChoiceField(label="项目名称",queryset=Project.objects.all())
    interfName = forms.CharField(max_length=30,label="接口名称")
    interfDns = forms.URLField(max_length=30,label="请求地址")
    interfPath = forms.CharField(max_length=50,label="路径")
    interfMethod = forms.CharField(widget=forms.widgets.Select(choices=METHOD_TYPE),label="请求方法")
    interfParams = forms.CharField(max_length=255,label="请求参数",widget=forms.Textarea)
    excuteResult = forms.CharField(max_length=5,label="执行结果",required=False)
    name = forms.ModelChoiceField(label="测试负责人",queryset=Owner.objects.all().filter(role='测试'))
    summary  = forms.ModelChoiceField(label="用例摘要",queryset=Case.objects.all())

class CaseForm(forms.Form):
    projectName = forms.ModelChoiceField(label="开发负责人",queryset=Project.objects.all())
    name = forms.ModelChoiceField(label="开发负责人",queryset=Owner.objects.all().filter(role='测试'))
    summary = forms.CharField(max_length=100,label="用例摘要", widget=forms.TextInput(attrs={'class':'span10'}))
    details = forms.CharField(max_length=255,label="用例详情",widget=forms.Textarea(attrs={'class':'span10'}),required=False)

class OwnerForm(forms.Form):
    ROLE_TYPE=(('测试','测试'),('开发','开发'),)
    name = forms.CharField(max_length=20,label=u"姓名")
    um = forms.CharField(max_length=30,label=u"um账号",required=False)
    role = forms.CharField(widget=forms.widgets.Select(choices=ROLE_TYPE),label=u"角色",required=True)

class ProjectForm(forms.Form):
    # dev = []
    # proj_role = list(Owner.objects.values_list("id").filter(role='开发'))
    # for i in range(len(owners)):
    #     dev.append((owners[i][0],owners[i][0]))
    projectName = forms.CharField(max_length=20,label="项目名称")
    name = forms.ModelChoiceField(label="开发负责人",queryset=Owner.objects.all().filter(role='开发'))







