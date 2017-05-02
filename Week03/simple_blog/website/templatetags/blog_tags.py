from django import template
from markdown import Markdown

register = template.Library()


@register.filter
def markdown(value):
    html = Markdown()
    return html.convert(value)
