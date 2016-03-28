from django.shortcuts import render
from django.http import JsonResponse
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