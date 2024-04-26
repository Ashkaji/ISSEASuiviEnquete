from django import template

register = template.Library()


@register.filter
def lastfirstname(value):
    if not value:
        return ''

    words = value.split(' ')
    return words[-1]
