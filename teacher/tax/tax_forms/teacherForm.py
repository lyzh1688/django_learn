#coding=utf-8
__author__ = 'Administrator'
from django import forms
from tax.models import Teacher
from django.core.exceptions import ValidationError

class TeacherForm(forms.ModelForm):

    def __init__(self, *args, **kwarg):
        super(TeacherForm, self).__init__(*args, **kwarg)
        self.fields['name'].required = True
        #self.fields['name'].validators.append(validate_teacher)
        self.fields['name'].error_messages={'required':u'请输入姓名!'}
        self.fields['isFullTime'].required = True
        #name = forms.CharField(required=True,validators=[validate_teacher])

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