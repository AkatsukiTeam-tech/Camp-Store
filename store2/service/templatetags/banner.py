from django import template

register = template.Library()

@register.inclusion_tag('tags/banner.html')
def banner_tag(object):
    return {'banner' : object}