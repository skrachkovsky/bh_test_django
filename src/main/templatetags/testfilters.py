from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='filter1')
def filter1(value):
    return value + ' atata'
