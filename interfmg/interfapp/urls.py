"""interfmg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from interfapp import views

urlpatterns = [
    url(r'^project_conf/',views.pro_query,name='project_conf'),
    url(r'^owner_conf/',views.owner_qurey,name='owner_conf'),
    url(r'^case_query/',views.case_query,name='case_query'),
    url(r'^interface_conf/',views.interface_query,name='interface_conf'),
    url(r'^case_edit/',views.case_update,name='case_edit'),
    url(r'^project_delete/',views.project_delete,name='project_delete'),
    url(r'^project_update/',views.project_update,name='project_update'),
    url(r'^project_add/',views.project_update,name='project_add'),
    url(r'^owcf/$',views.owqry,name='owcf'),
    url(r'^owadd/$',views.owadd,name='owadd'),
    url(r'^owdel-(?P<id>\d+)/$',views.owdel,name='owdel'),
]
