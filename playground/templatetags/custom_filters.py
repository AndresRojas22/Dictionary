from django import template

register = template.Library()

@register.filter(name='custom_replace')
def custom_replace (value):
    return value.replace("/","")