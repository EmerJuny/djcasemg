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
import requests
import  json
import copy
from django.db.models.deletion import ProtectedError
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
            name = data['name']
            data = Project(projectName = projectName,name=name)
            data.save()
            return HttpResponseRedirect('/interfapp/projconf/')
        else:
            return render_to_response("projadd.html", locals(), RequestContext(request))
    else:
        form = ProjectForm()
        return render_to_response('projadd.html', {'form': form}, context_instance=RequestContext(request))

def projdel(request,id):
    entry = get_object_or_404(Project,pk=int(id))
    p = Project.objects.get(id=id)
    if (  p.case_set.all().count()>0 ) :
        return HttpResponse('有关联项不能删除')
    else:
        entry.delete()
        return HttpResponseRedirect('/interfapp/projconf')

@csrf_exempt
def projupd(request,id):
    if request.method=='POST':
        projectName = request.POST['projectName']
        name = request.POST['name']
        owner = Owner.objects.get(name=name)
        Project.objects.filter(id=int(id)).update(projectName=projectName,name=owner.id)
        return HttpResponseRedirect('/interfapp/projconf/')
    else:
        data = Project.objects.filter(id=int(id))
        names = Owner.objects.filter(role='开发')
        return  render(request,'projupd.html',locals())

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
    p = Owner.objects.get(id=id)
    if ( ( p.project_set.all().count()>0) or (p.case_set.all())>0 ) :
        return HttpResponse('有关联项不能删除')
    else:
        print('无关联',entry)
        entry.delete()
        return HttpResponseRedirect('/interfapp/owcf/')

@csrf_exempt
def owupd(request,id):
    if request.method=='POST':
        name = request.POST['name1']
        um = request.POST['um']
        print (name)
        Owner.objects.filter(id=int(id)).update(name=name,um=um)
        return HttpResponseRedirect('/interfapp/owcf/')
    else:
        data = Owner.objects.filter(id=int(id))
        return  render(request,'owupd.html',{'data':data})

def intfcf(request):
    limit = 10 # 每页显示的记录数
    data = Interfaces.objects.all().order_by("interfName")
    paginator = Paginator(data, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        data = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('intfcf.html',{'data':data})

@csrf_exempt
def intfadd(request):
    # error = []
    if request.method == 'POST':
        form = InterfaceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            projectName = data['projectName']
            interfName = data['interfName']
            interfDns = data['interfDns']
            interfPath = data['interfPath']
            interfMethod = data['interfMethod']
            interfParams = data['interfParams']
            data = Interfaces(projectName=projectName,interfName=interfName,interfDns=interfDns,
             interfPath=interfPath,interfParams=interfParams,interfMethod=interfMethod)
            data.save()
            return HttpResponseRedirect('/interfapp/intfcf/')
        else:
            return render_to_response("intfadd.html", locals(), RequestContext(request))
    else:
        form = InterfaceForm()
        return render_to_response('intfadd.html', {'form': form}, context_instance=RequestContext(request))

def intfrun(request,id):
    reqobj = Case.objects.filter(id=id)
    return render(request,'intfrun.html',{'data':reqobj})

@csrf_exempt
def intfupd(request,id):
    if request.method=='POST':
        interfName = request.POST['interfName']
        interfParams = request.POST['interfParams']
        Interfaces.objects.filter(id=int(id)).update(interfName=interfName,interfParams=interfParams)
        return HttpResponseRedirect('/interfapp/intfcf')
    else:
        data = Interfaces.objects.filter(id=int(id))
        return render(request,'intfupd.html',{'data':data})

@csrf_exempt
# 复制接口同时打开编辑页面
def intfclo(request,id):
    if request.method=='POST':
        interfName = request.POST['interfName']
        interfPath = request.POST['interfPath']
        interfParams = request.POST['interfParams']
        t= copy.deepcopy(Interfaces.objects.get(pk=int(id)))
        t.interfName=interfName
        t.interfPath=interfPath
        t.interfParams=interfParams
        t.pk=None
        t.save()
        return HttpResponseRedirect('/interfapp/intfcf')
    else:
        data = Interfaces.objects.filter(id=int(id))
        return render(request,'intfupd.html',{'data':data})

# 发送请求
@csrf_exempt
def sendreq(request):
    if request.method=='GET':
        url = request.GET['url']
        responses = requests.get(url)
        return HttpResponse(responses.text)
    else:
        id = request.POST['id']
        datas = Interfaces.objects.filter(id=int(id))
        for i in datas:
            url1=i.interfDns
            url2=i.interfPath
            data=i.interfParams
        url=(url1+'/'+url2).encode('utf-8')
        # 添加header
        headers1 = {'Content-Type':'application/x-www-form-urlencoded'}
        data1=eval(data) #将unicode类型转换为字典类型
        responses = requests.post(url,headers=headers1,data=data1)
        return HttpResponse(responses)

def intfdel(request,id):
    x = get_object_or_404(Interfaces,pk=int(id))
    p = Interfaces.objects.get(id=id)
    if ( p.case_set.all().count()>0)  :
        return HttpResponse('有关联项不能删除')
    else:
        print('无关联',p)
        p.delete()
    return HttpResponseRedirect('/interfapp/intfcf/')

def casecf(request):
    limit = 10 # 每页显示的记录数
    data = Case.objects.all().order_by("summary") #.values('id','summary','details','owner','project')
    paginator = Paginator(data, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码

    try:
        data = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render_to_response('casecf.html',locals())

@csrf_exempt
def caseadd(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            summary = data['summary']
            details = data['details']
            name = data['name']
            projectName = data['projectName']
            checkPoint = data['checkPoint']
            interfName=data['interfName']
            data = Case(summary=summary,details=details,projectName=projectName,name=name,checkPoint=checkPoint,interfName=interfName)
            data.save()
            return HttpResponseRedirect('/interfapp/casecf/')
        else:
            return render_to_response("caseadd.html", locals(), RequestContext(request))
    else:
        form = CaseForm()
        return render_to_response('caseadd.html', {'form': form}, context_instance=RequestContext(request))

def casedel(request,id):
    entry = get_object_or_404(Case,pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/interfapp/casecf/')

def caseupd(request,id):
    if request.method=='POST':
        # interfParams = request.POST['interfParams']
        checkPoint = request.POST['checkPoint']
        summary = request.POST['summary']
        t =Case.objects.get(id=int(id))
        print(t.interfName.id)
        # Interfaces.objects.filter(id=t.interfName.id).update(interfParams=interfParams)
        Case.objects.filter(id=int(id)).update(checkPoint=checkPoint,summary=summary)

        return HttpResponseRedirect('/interfapp/casecf')
    else:
        data = Case.objects.filter(id=int(id))
        return render(request,'caseupd.html',{'data':data})

# 用例查询
def caseqry(request):
    data1 = Case.objects.all()
    if request.method=='GET':
        limit = 10
        id = request.GET['id']
        interfName=request.GET['interfName']
        print (interfName)
        projectName=request.GET['projectName']
        # actname = Interfaces.objects.get(id=interfName)
        # print (actname.interfName)
        print (id)
        print(int(id)>0)
        if int(id)>0 :
            data = Case.objects.filter(id=id).order_by("summary")
        # elif interfName is not None  and projectName is not None:
        #     data = Case.objects.filter(projectName=projectName,interfName_id=interfName).order_by("summary")
        # elif interfName is not None:
        #     data = Case.objects.filter(interfName_id=interfName).order_by("summary")
        # else:
        #     data = Case.objects.all()
        paginator = Paginator(data, limit)  # 实例化一个分页对象
        page = request.GET.get('page')  # 获取页码
        try:
            data = paginator.page(page)  # 获取某页对应的记录
        except PageNotAnInteger:  # 如果页码不是个整数
            data = paginator.page(1)  # 取第一页的记录
        except EmptyPage:  # 如果页码太大，没有相应的记录
            data = paginator.page(paginator.num_pages)
    return render(request,'casecf.html',locals())
@csrf_exempt
def caseclo(request,id):
    if request.method=='POST':
        interfParams = request.POST['interfParams']
        checkPoint = request.POST['checkPoint']
        summary = request.POST['summary']
        interfName = request.POST['interfName']
        # Case.objects.filter(id=int(id)).update(checkPoint=checkPoint,summary=summary)
        # Interfaces.objects.filter(interfName=interfName).update(interfParams=interfParams)
        s1=Case.objects.get(id=int(id))
        s =copy.deepcopy(s1)
        t = copy.deepcopy(Interfaces.objects.get(id=s1.interfName.id))
        print('修改前：',t.id)
        t.interfParams=interfParams
        t.pk = None
        t.save()
        print('修改后:',t.id)
        s.summary=summary
        s.checkPoint=checkPoint
        s.interfName_id = t.id
        s.pk=None
        s.save()
        return HttpResponseRedirect('/interfapp/casecf')
    else:
        data = Case.objects.filter(id=int(id))
        return render(request,'caseupd.html',{'data':data})




