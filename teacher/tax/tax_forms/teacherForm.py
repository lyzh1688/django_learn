#coding=utf-8
__author__ = 'Administrator'
from django import forms
from tax.models import Teacher
from django.core.exceptions import ValidationError

class TeacherFormMixin():
    def clean_status(self):
        status = self.cleaned_data.get("status")
        if not status:
            status = True
        return status

class TeacherUpdateForm(TeacherFormMixin,forms.ModelForm):
    def __init__(self, *args, **kwarg):
        super(TeacherUpdateForm, self).__init__(*args, **kwarg)
        self.fields['name'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-medium'}))
        self.fields['isFullTime'] = forms.ChoiceField(label=(u"是否全职"),required=True,initial=True, choices=((False, u'否'), (True, u'是')))
        self.fields['status'] = forms.BooleanField(required=False,initial=True)

    class Meta:
        model = Teacher
        #fields = ('name', 'isFullTime')
        fields = '__all__'


class TeacherCreateForm(TeacherFormMixin,forms.ModelForm):
    def __init__(self, *args, **kwarg):
        super(TeacherCreateForm, self).__init__(*args, **kwarg)
        self.fields['name'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-medium'}))
        self.fields['isFullTime'] = forms.ChoiceField(label=(u"是否全职"),required=True,initial=True, choices=((False, u'否'), (True, u'是')))
        self.fields['status'] = forms.BooleanField(required=False,initial=True)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError(u'%s请输入姓名')
        if len(Teacher.objects.filter(name=name)) > 0:
            raise forms.ValidationError(u'%s用户已经存在')
            #raise ValidationError(_(u'%s用户已经存在'))

        return name

    class Meta:
        model = Teacher
        #fields = ('name', 'isFullTime')
        fields = '__all__'


