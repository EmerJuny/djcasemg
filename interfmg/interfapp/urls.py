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
    url(r'^intfcf/',views.intfcf,name='intfcf'),
    url(r'^intfadd/$',views.intfadd,name='intfadd'),
    url(r'^intfrun-(?P<id>\d+)/$',views.intfrun,name='intfrun'),
    url(r'^intfrun/$',views.intfrun,name='intfrun'),
    url(r'^sendreq/$',views.sendreq,name='sendreq'),
    url(r'^intfdel-(?P<id>\d+)/$',views.intfdel,name='intfdel'),
    # url(r'^projdel/',views.projdel,name='projdel'),
    url(r'^projconf/$',views.projconf,name='projconf'),
    url(r'^projadd/$',views.projadd,name='projadd'),
    url(r'^projdel-(?P<id>\d+)/$',views.projdel,name='projdel'),
    url(r'^projupd/',views.projupd,name='projupd'),
    url(r'^owcf/$',views.owqry,name='owcf'),
    url(r'^owadd/$',views.owadd,name='owadd'),
    url(r'^owdel-(?P<id>\d+)/$',views.owdel,name='owdel'),
    url(r'^casecf/$',views.casecf,name='casecf'),
    url(r'^caseadd/$',views.caseadd,name='caseadd'),
    url(r'^casedel-(?P<id>\d+)/$',views.casedel,name='casedel'),
    url(r'^caseupd/',views.caseupd,name='caseupd'),

]
