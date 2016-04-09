__author__ = 'Administrator'
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView

from tax.models import Teacher
from tax.tax_forms.teacherForm import TeacherCreateForm,TeacherUpdateForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from teacher.util.util import *

class UpdateTeacher(UpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    template_name = 'teacher_add.html'
    success_url = '/teacher'

class AddTeacher(CreateView):
    form_class = TeacherCreateForm
    model = Teacher
    #template_name = 'addteacher.html'
    template_name = 'teacher_add.html'
    def post(self, request, *args, **kwargs):
        objTeacherForm = TeacherCreateForm(self.request.POST)
        if objTeacherForm.is_valid():
            new_teacher = objTeacherForm.save()
            return redirect(reverse("teacherlist"))
        else:
            return redirect(reverse("teacheradd"),{'form': objTeacherForm})

class ListTeacher(ListView):
    context_object_name = 'teacherlist'
    template_name = 'teacher.html'
    paginate_by = 10
    http_method_names = [u'get',]

    def get_queryset(self):
        #teacherlist = Teacher.objects.all()
        name = self.request.GET.get('name')
        isFullTime = self.request.GET.get('isFullTime')
        status = 1
        searchCondition = {'name':name,'isFullTime':isFullTime,'status':status}
        kwargs = SearchParamUtil.getKwargs(searchCondition)
        try:
            teacherlist = Teacher.objects.filter(**kwargs)
        except Model.DoesNotExist:
            print "ModelDoesNotExist"
        return teacherlist