# custom_filters.py

from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter(name='preserve_whitespace')
@stringfilter
def preserve_whitespace(value):
    # Replace multiple consecutive spaces with non-breaking spaces (&nbsp;)
    # Replace newline characters with <br> tags
    # Wrap the result in <pre> tags to preserve all whitespace and formatting
    value = re.sub(r'\s+', lambda m: '&nbsp;' * len(m.group(0)), value)
    value = value.replace('\n', '<br>')
    return f'{value}'
