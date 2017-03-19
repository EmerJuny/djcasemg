# coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from interfapp.interface_form import InterfaceForm,ProjectForm,CaseForm,OwnerForm
from interfapp.models import Project,Interfaces
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def pro_query(request):
    #分页处理
    limit = 10
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
    return render_to_response('project_conf.html',{'data':data})

def interface_query(request):
    pass

def interface_add(request):
    pass
def owner_qurey(request):
    pass
def case_query(request):
    pass
def case_update(request):
    pass
def project_delete(request):
    pass
def project_update(request):
    pass