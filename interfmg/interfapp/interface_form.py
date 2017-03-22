# coding=utf-8
from django import forms
from interfapp.models import Interfaces,Case,Owner

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
    summary = forms.CharField(max_length=100,label="用例摘要")
    details = forms.CharField(max_length=255,label="用例详情",widget=forms.Textarea,required=False)
    owner = forms.CharField(max_length=20,label="创建人")
    state  = forms.CharField(max_length=10,label="状态")
    operate = forms.CharField(max_length=10,label="操作")

class OwnerForm(forms.Form):
    # def __init__(self,*args,**kwargs):
    #     super(OwnerForm,self).__init__(*args,**kwargs)
    ROLE_TYPE=(('测试','测试'),('开发','开发'),)
    name = forms.CharField(max_length=20,label="姓名")
    um = forms.CharField(max_length=30,label="um账号",required=False)
    role = forms.CharField(widget=forms.widgets.Select(choices=ROLE_TYPE),label="角色",required=True)


class ProjectForm(forms.Form):
    #def __init__(self, *args, **kwargs):
    #    super(ProjectForm, self).__init__(*args, **kwargs)

    projectName = forms.CharField(max_length=20,label="项目名称")
    owner = forms.CharField(max_length=20,label="开发负责人")






