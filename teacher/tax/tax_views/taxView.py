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
from django.db.models import Q, Model
import time
from tax.logic.taxCalc import TaxCalc

class TeacherTaxView(ListView):
    context_object_name = 'teachertaxlist'
    template_name = 'tax.html'
    http_method_names = [u'get',]

    def get_context_data(self, **kwargs):
        context = super(TeacherTaxView, self).get_context_data(**kwargs)
        date = self.kwargs.get('date')
        if not date:
            date = time.strftime('%Y%m',time.localtime(time.time()))
        context['date'] = date
        return context

    def get_queryset(self):
        date = self.kwargs.get('date')
        if not date:
            date = time.strftime('%Y%m',time.localtime(time.time()))

        try:
            sql = '''
                  select
                  t.id,
                  max(t.name) as name ,
                  max(t.isFullTime) as isFullTime ,
                  sum(c.fee * r.times) as cost
                  from tax_teacher t,tax_class c,tax_record r
                  where t.id = c.teacher_id
                  and c.id = r.clazz_id
                  and r.date = %s
                  group by t.id
                '''%date

            cursor = connection.cursor()
            cursor.execute(sql)
            fetchall = cursor.fetchall()
            teachertaxlist = []
            for obj in fetchall:
                dic = {}
                dic['id'] = obj[0]
                dic['name'] = obj[1]
                dic['isFullTime'] = obj[2]
                dic['cost'] = obj[3]
                dic['tax'] = TaxCalc.taxCalc(dic['isFullTime'],dic['cost'])
                dic['realCost'] = dic['tax'] + dic['cost']
                teachertaxlist.append(dic)

        except Model.DoesNotExist:
            print "ModelDoesNotExist"
        return teachertaxlist