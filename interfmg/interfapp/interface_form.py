# coding=utf-8
from django import forms
from interfapp.models import Interfaces,Case,Owner,Project
from django.forms import ModelForm,Textarea
from django.utils.translation import ugettext_lazy as _
class InterfaceForm(forms.Form):
    project = forms.CharField(max_length=20,label="项目名称")
    interfName = forms.CharField(max_length=30,label="接口名称")
    interfDns = forms.URLField(max_length=30,label="请求地址")
    interfPath = forms.CharField(max_length=50,label="路径")
    interfMethod = forms.CharField(max_length=10,label="请求方法")
    interfParams = forms.CharField(max_length=255,label="请求参数",widget=forms.Textarea)
    excuteResult = forms.CharField(max_length=30,label="执行结果",required=False)
    owner = forms.CharField(max_length=30,label="负责人")
    caseSummary  = forms.CharField(max_length=30,label="用例摘要")
    operate = forms.CharField(max_length=10,label="操作")

class CaseForm(forms.Form):
    pn,ow =[],[]
    proname_list = list(Project.objects.values_list("projectName"))
    ow_list = list(Owner.objects.values_list("name").filter(role='测试'))
    for i in range(len(proname_list)):
        pn.append((proname_list[i][0],proname_list[i][0]))
    for j in range(len(ow_list)):
        ow.append((ow_list[j][0],ow_list[j][0]))
    id = forms.IntegerField(label="用例编号")
    projectName = forms.CharField(widget=forms.widgets.Select(choices=pn),label="所属项目")
    owner = forms.CharField(widget=forms.widgets.Select(choices=ow),label="创建人")
    summary = forms.CharField(max_length=100,label="用例摘要")
    details = forms.CharField(max_length=255,label="用例详情",widget=forms.Textarea,required=False)

class OwnerForm(forms.Form):
    # def __init__(self,*args,**kwargs):
    #     super(OwnerForm,self).__init__(*args,**kwargs)
    ROLE_TYPE=(('测试','测试'),('开发','开发'),)
    name = forms.CharField(max_length=20,label=u"姓名")
    um = forms.CharField(max_length=30,label=u"um账号",required=False)
    role = forms.CharField(widget=forms.widgets.Select(choices=ROLE_TYPE),label=u"角色",required=True)


class ProjectForm(forms.Form):
    #def __init__(self, *args, **kwargs):
    #    super(ProjectForm, self).__init__(*args, **kwargs)
    dev = []
    owners = list(Owner.objects.values_list("name").filter(role='开发'))
    for i in range(len(owners)):
        dev.append((owners[i][0],owners[i][0]))
    projectName = forms.CharField(max_length=20,label="项目名称")
    owner = forms.CharField(widget=forms.widgets.Select(choices=dev),label="开发负责人",required=True)






