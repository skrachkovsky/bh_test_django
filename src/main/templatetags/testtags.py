from django import template

register = template.Library()


@register.simple_tag(name='tag1')
def tag1(val1, val2=None):
    return val1.upper()


@register.inclusion_tag('main/tag2.html')
def tag2(val1):
    return {
        'val1': val1
    }

