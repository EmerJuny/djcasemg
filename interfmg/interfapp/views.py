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





def intfcf(request):
    limit = 10 # 每页显示的记录数
    data = Interfaces.objects.all().order_by("id")
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
        # projectName = request.POST['projectName']
        # interfDns = request.POST['interfDns']
        # interfPath = request.POST['interfPath']
        # interfMethod = request.POST['interfMethod']
        interfParams = request.POST['interfParams']
        print interfName
        Interfaces.objects.filter(id=int(id)).update(interfName=interfName,
                   #                                   projectName=projectName,interfDns=interfDns,
                   # interfPath=interfPath,interfMethod=interfMethod,
                                                     interfParams=interfParams)
        return HttpResponseRedirect('interfapp/intfcf')
    else:
        data = Interfaces.objects.filter(id=int(id))
        return render(request,'intfupd.html',{'data':data})

@csrf_exempt
def sendreq(request):
    # if request.method=='GET':
    #  url = request.GET['url']
    #     mpra= request.GET['data']
    #     print mpra
    #     responses = requests.get(url)
    #     return HttpResponse(responses.text)
    #     url = request.POST['url']
    #     data= request.POST['data']
    #     url1 = url.encode('utf-8')
    #     data1 = eval(data.encode('utf-8'))
        id = request.POST['id']
        datas = Interfaces.objects.filter(id=int(id))
        for i in datas:
            url1=i.interfDns
            url2=i.interfPath
            data=i.interfParams
        url=(url1+'/'+url2).encode('utf-8')

        headers1 = {'Content-Type':'application/x-www-form-urlencoded'}
        print 'interfParams:',data
        # h1=headers1.encode('utf-8')
        # headers = eval(h1)
        data1=eval(data)
        print 'data:',data1
        responses = requests.post(url,headers=headers1,data=data1)
        # print 'resp:',responses.text
        return HttpResponse(responses)

def intfdel(request,id):
    p = get_object_or_404(Interfaces,pk=int(id))
    p = Owner.objects.get(id=id)
    if ( p.case_set.all().count()>0)  :
        return HttpResponse('有关联项不能删除')
    else:
        print('无关联',p)
        p.delete()
    return HttpResponseRedirect('/interfapp/intfcf/')

def casecf(request):
    limit = 10 # 每页显示的记录数
    data = Case.objects.all().order_by("id") #.values('id','summary','details','owner','project')
    print type(data)
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
    error = []
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # id = data['id']
            summary = data['summary']
            details = data['details']
            name = data['name']
            projectName = data['projectName']
            checkPoint = data['checkPoint']
            interfName=data['interfName']
            data = Case(summary=summary,details=details,name=name,projectName=projectName,checkPoint=checkPoint,interfName=interfName)
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

def caseupd(request):
    pass
    # X.save(update_fields=['fields'])  更新时指定列保存


def projupd(request):
    pass


