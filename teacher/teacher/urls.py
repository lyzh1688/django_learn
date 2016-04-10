"""teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from tax import views as tax_views
from tax.tax_views import teacherView
from tax.tax_views import courseView
from tax.tax_views import recordView
from tax.tax_views import taxView
from django.contrib.auth.decorators import login_required
import settings
urlpatterns = [

    ###################################################
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':  settings.STATIC_ROOT ,'show_indexes': True} ) ,
    url(r'^admin/', admin.site.urls),
    url(r'^teacher/$', login_required(teacherView.ListTeacher.as_view()), name = 'teacherlist'),
    url(r'^teacher/add/$', login_required(teacherView.AddTeacher.as_view()), name = 'teacheradd'),
    url(r'^teacher/edit/(?P<pk>\w+)/$', login_required(teacherView.UpdateTeacher.as_view()),name = 'teacheredit'),
    url(r'^teacher/del/$', tax_views.DelTeacher,name = 'teacherdel'),
    url(r'^course/$', tax_views.CourseDetail, name = 'course'),
    #url(r'^course/detail/(?P<id>\w+)/$', courseView.DetailCourse.as_view(),name = 'coursedetail'),

    url(r'^course/detail/(?P<id>\w+)/$', login_required(courseView.ListClassTeacher.as_view()),name = 'coursedetail'),
    url(r'^course/edit/detail/(?P<id>\w+)/$', login_required(courseView.DetailCourse.as_view()),name = 'coursedetailedit'),
    url(r'^course/edit/fee/$', tax_views.EditFee,name = 'courseeditfee'),

    url(r'^course/edit/submit/$', tax_views.FeeFormSubmit,name = 'coursedetaileditsubmit'),
    url(r'^class/del/$', tax_views.DelClass,name = 'classdel'),

    url(r'^record/$', login_required(recordView.RecordIndex.as_view()),name = 'record'),
    url(r'^record/detail/(?P<id>\w+)/(?P<date>\w+)$', login_required(recordView.RecordDetail.as_view()),name = 'recorddetail'),
    url(r'^record/settimes/$', tax_views.SetTimes,name = 'settimes'),
    url(r'^tax/$', login_required(taxView.TeacherTaxView.as_view()),name = 'tax'),
    url(r'^tax/(?P<date>\w+)/$', login_required(taxView.TeacherTaxView.as_view()),name = 'taxwithdate'),
    url(r'^download/$', tax_views.ExcelExport,name = 'excelExport'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
]
