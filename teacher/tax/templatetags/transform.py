#coding=utf-8
from django import template
register = template.Library()

@register.filter(name='bool_trans')
def bool_trans(value,arg=None):
    if value == 'True' or value == True:
        return u'是'
    else:
        return u'否'
