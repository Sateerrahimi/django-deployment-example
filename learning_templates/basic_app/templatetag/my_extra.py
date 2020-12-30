from django import template

register = template.Library()

def cut(value, tag):
    return value.replace(arg,'')
register.filter('cut',cut)
