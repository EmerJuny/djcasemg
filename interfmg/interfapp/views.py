# coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from interfapp.interface_form import InterfaceForm,ProjectForm,CaseForm,OwnerForm
from interfapp.models import Project,Interfaces,Case
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django import  forms
from interfapp.models import Owner
# Create your views here.

def projconf(request):
    #分页处理
    limit = 15
    data = Project.objects.all()
    paginator = Paginator(data,limit)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    #取数
    return render_to_response('projconf.html',{'data':data})

@csrf_exempt
def projadd(request):
    error = []
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            projectName = data['projectName']
            owner = data['owner']
            data = Project(projectName = projectName,owner=owner)
            data.save()
            return HttpResponseRedirect('/interfapp/projconf/')
        else:
            return render_to_response("projadd.html", locals(), RequestContext(request))
    else:
        form = ProjectForm()
        return render_to_response('projadd.html', {'form': form}, context_instance=RequestContext(request))

@csrf_exempt
def projdel(request,id):
    entry = get_object_or_404(Project,pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/interfapp/projconf/')


def owqry(request):
    limit = 15 # 每页显示的记录数
    data = Owner.objects.all().order_by("id")
    paginator = Paginator(data, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        data = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('owcf.html',{'data':data})

@csrf_exempt
def owadd(request):
    error = []
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # role_list = request.POST.getlist('role')
            name = data['name']
            um = data['um']
            role = data['role']
            data = Owner(name=name,um=um,role=role)
            data.save()
            return HttpResponseRedirect('/interfapp/owcf/')
        else:
            return render_to_response("owadd.html", locals(), RequestContext(request))
    else:
        form = OwnerForm()
        return render_to_response('owadd.html', {'form': form}, context_instance=RequestContext(request))

@csrf_exempt
def owdel(request,id):
    entry = get_object_or_404(Owner,pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/interfapp/owcf/')





def interface_query(request):
    pass

def interface_add(request):
    pass



def casecf(request):
    limit = 10 # 每页显示的记录数
    data = Case.objects.all().values('id','summary','details','owner','project','createtime').order_by("id")
    paginator = Paginator(data, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        data = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('casecf.html',{'data':data})

@csrf_exempt
def caseadd(request):
    error = []
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            id = data['id']
            summary = data['summary']
            details = data['details']
            owner = data['owner']
            project = data['project']
            # createtime = data['createtime']
            # lastUpdateTime = data['lastUpdateTime'] ,createtime=createtime,lastUpdateTime=lastUpdateTime
            data = Owner(id=id,summary=summary,details=details,role=owner,project=project)
            data.save()
            return HttpResponseRedirect('/interfapp/casecf/')
        else:
            return render_to_response("caseadd.html", locals(), RequestContext(request))
    else:
        form = CaseForm()
        proname_list = Project.objects.values_list("projectName")
        ow_list = Owner.objects.values_list("name").filter(role='测试')
        return render_to_response('caseadd.html', {'form': form}, context_instance=RequestContext(request))

def casedel(request):
    entry = get_object_or_404(Case,pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/interfapp/casecf/')

def caseupd(request):
    pass



def projupd(request):
    pass

