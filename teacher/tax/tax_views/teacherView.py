__author__ = 'Administrator'
from django.views.generic.edit import CreateView
from tax.models import Teacher
from tax.tax_forms.teacherForm import TeacherForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

class AddTeacher(CreateView):
    form_class = TeacherForm
    model = Teacher
    template_name = 'addteacher.html'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        objTeacherForm = TeacherForm(self.request.POST)
        if objTeacherForm.is_valid():
            new_teacher = objTeacherForm.save()
            return HttpResponseRedirect('/success')
        else:

            return redirect(reverse("addteacher"),{'form': objTeacherForm})
