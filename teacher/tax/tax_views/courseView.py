
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import TemplateView
from tax.tax_forms.feeForm import FeeForm
from django.views.generic.detail import SingleObjectMixin
from tax.models import Class
from tax.models import Course
from tax.models import Teacher
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from teacher.util.util import *
from django.db import connection,transaction
from django.db.models import Q,Model

class ListClassTeacher(ListView):
    context_object_name = 'classteacherlist'
    template_name = 'coursedetail.html'
    paginate_by = 10
    http_method_names = [u'get',]

    def get_context_data(self, **kwargs):
        context = super(ListClassTeacher, self).get_context_data(**kwargs)
        course_id = self.kwargs.get('id')
        context['course_id'] = course_id
        context['course_name'] = Course.objects.get(id=course_id).name
        return context

    def get_queryset(self):
        course_id = self.kwargs.get('id')
        try:
            sql = '''
                  select t.id,t.name,t.isFullTime,c.fee
                    from tax_teacher t,tax_class c
                    where c.course_id = %s
                    and c.teacher_id = t.id
                    and t.status = 1
                '''%course_id

            cursor = connection.cursor()
            cursor.execute(sql)
            fetchall = cursor.fetchall()
            classteacherlist = []
            for obj in fetchall:
                dic = {}
                dic['id'] = obj[0]
                dic['name'] = obj[1]
                dic['isFullTime'] = obj[2]
                dic['fee'] = obj[3]
                classteacherlist.append(dic)

        except Model.DoesNotExist:
            print "ModelDoesNotExist"
        return classteacherlist

class DetailCourse(TemplateView):
    #context_object_name = 'detail'
    template_name = 'coursedetailedit.html'
    http_method_names = [u'get',u'post']
    def get_context_data(self, **kwargs):
        id = self.kwargs.get('id')
        name = self.request.GET.get('name')
        isshowall = self.request.GET.get('isshowall')
        context = super(DetailCourse, self).get_context_data(**kwargs)
        if name:
            teacher_to_select = Teacher.objects.exclude(ClassTeacher__course_id=id).filter(Q(name__contains=name)&Q(status=1))
        else:
            if isshowall == '1':
                teacher_to_select = Teacher.objects.exclude(ClassTeacher__course_id=id).filter(Q(status=1))
            else:
                teacher_to_select = Teacher.objects.exclude(ClassTeacher__course_id=id).filter(Q(status=1))[0:9]

        context['detail'] = {'teacher_to_select':teacher_to_select,'course_id':id}
        return context

'''
class DetailCourseEdit(TemplateView):
    template_name = 'coursedetailedit.html'
    http_method_names = [u'get',u'post']

    def post(self, request, *args, **kwargs):
        print '---------------------------------'
        teacherid = self.request.POST.get('teacherid')
        courseid = self.request.POST.get('courseid')
        teacherfee = self.request.POST.get('teacherfee')
        print '---------------------------------'
        print teacherid
        teacher = Teacher.objects.get(id=teacherid)
        course = Course.objects.get(id=courseid)
        clazz = Class(teacher=teacher,course=course,fee=teacherfee)
        feeForm = FeeForm( instance=clazz)
        feeForm.save()
        return redirect(reverse("coursedetail"))
'''