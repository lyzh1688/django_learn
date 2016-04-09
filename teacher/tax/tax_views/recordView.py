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
from django.db.models import Q
class RecordIndex(TemplateView):
    #context_object_name = 'detail'
    template_name = 'record.html'
    http_method_names = [u'get',u'post']
    def get_context_data(self, **kwargs):

        context = super(RecordIndex, self).get_context_data(**kwargs)
        course_to_select = Course.objects.all()
        context['record'] = {'course_to_select':course_to_select}
        return context

class RecordDetail(TemplateView):
    #context_object_name = 'detail'
    template_name = 'recordlist.html'
    http_method_names = [u'get',u'post']
    def get_context_data(self, **kwargs):
        context = super(RecordDetail, self).get_context_data(**kwargs)

        course_id = self.kwargs.get('id')
        date = self.kwargs.get('date')
        course_name = Course.objects.get(id=course_id).name
        sql = '''
         select t.id,t.name,t.isFullTime,c.fee,r.times
            from tax_teacher t,tax_class c
                    left join  tax_record r
                    on r.clazz_id = c.id
                    and r.date = %s
                    where c.course_id = %s
                    and c.teacher_id = t.id
                    and t.status = 1
        '''%(date,course_id)
        cursor = connection.cursor()
        cursor.execute(sql)
        fetchall = cursor.fetchall()
        teacher_to_edit = []
        for obj in fetchall:
            dic = {}
            dic['id'] = obj[0]
            dic['name'] = obj[1]
            dic['isFullTime'] = obj[2]
            dic['fee'] = obj[3]
            dic['times'] = obj[4]

            teacher_to_edit.append(dic)

        context['record'] = {'teacher_to_edit':teacher_to_edit,
                              'course_id':course_id,
                              'course_name':course_name,
                             'date':date}
        return context