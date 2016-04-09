#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from tax.tax_forms.feeForm import *
from django.db.models import Q

from tax.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def hello(request):
    name = request.GET['name']
    return  render(request, 'hello.html', {"name":name})

def test(request):
    name_dict = {'name': 'Jennifer'}
    return JsonResponse(name_dict)


def success(request):
    return  render(request, 'success.html')

def error(request):
    return  render(request, 'error.html')

def index(request):
    return  render(request,'index.html')

def teacher(request):
    return  render(request,'teacher.html')

def detail(request):
    print request.POST.get('teacherid')
    return render(request,'course.html')

def record(request):
    return render(request,'record.html')

###################################################
@login_required
def SetTimes(request):
    course_id = request.GET['name'].split('_')[0]
    teacher_id = request.GET['name'].split('_')[1]
    date = request.GET['name'].split('_')[2]
    times = request.GET['value']
    clazz = Class.objects.get(Q(course_id=course_id)&Q(teacher_id=teacher_id))
    record,created = Record.objects.update_or_create(clazz=clazz,date=date,defaults={'times': times},)
    return JsonResponse({'Result':True})

@login_required
def CourseDetail(request):
    return  render(request,'course.html')
@login_required
def DelClass(request):
    teacher_id = request.GET['teacher_id']
    course_id = request.GET['course_id']
    teacher = Teacher.objects.get(id=teacher_id)
    course = Course.objects.get(id=course_id)
    Class.objects.filter(Q(teacher=teacher)&Q(course=course)).delete()
    return JsonResponse({'Result':True})

@login_required
def DelTeacher(request):
    teacher_id = request.GET['teacher_id']
    Teacher.objects.filter(id=teacher_id).update(status=False)
    return JsonResponse({'Result':True})
@login_required
def EditFee(request):
    course_id = request.GET['name'].split('_')[0]
    teacher_id = request.GET['name'].split('_')[1]
    fee = request.GET['value']
    Class.objects.filter(Q(course_id=course_id),Q(teacher_id=teacher_id)).update(fee=fee)
    return JsonResponse({'Result':True})

@login_required
def FeeFormSubmit(request):
    if request.method == 'POST':
        teacherid = request.POST.get('teacherid')
        courseid = request.POST.get('courseid')
        teacherfee = request.POST.get('teacherfee')
        print teacherid
        teacher = Teacher.objects.get(id=teacherid)
        course = Course.objects.get(id=courseid)
        clazz = Class(teacher=teacher,course=course,fee=teacherfee)
        feeForm = FeeForm( instance=clazz)
        try:
            feeForm.save()
        except Exception as e:
            print e

        #form = ContactForm(request.POST) # 获取Post表单数据
        #if form.is_valid(): # 验证表单
        #    return HttpResponseRedirect('/') # 跳转
        #else:
        #   pass
            #form = ContactForm() #获得表单对象
    else:
        print 'no post'
    return render(request,'course.html')

