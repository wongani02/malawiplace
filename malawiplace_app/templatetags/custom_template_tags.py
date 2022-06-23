from django import template
from ..models import *


register = template.Library()


@register.inclusion_tag('malawiplace_app/blog_tag.html')
def recent_blogs(count=2):
    blog = Blog.objects.order_by('-date')[:count]
    return {'blog': blog}


@register.inclusion_tag('malawiplace_app/blog_tags_searched.html')
def recent_blogs_searched(count=3):
    blog = Blog.objects.order_by('-date')[:count]
    return {'blog': blog}

@register.inclusion_tag('malawiplace_app/blog_footer.html')
def recent_blogs_footer(count=5):
    blog = Blog.objects.order_by('-date')[:count]
    return {'blog': blog}

@register.inclusion_tag('malawiplace_app/contact_footer.html')
def contact_footer(count=1):
    contact = ContactDetail.objects.order_by('-company_name')[:count]
    return {'contact': contact}


@register.inclusion_tag('malawiplace_app/about_footer.html')
def about_footer(count=1):
    about = About.objects.order_by('-company_name')[:count]
    return {'about': about}
