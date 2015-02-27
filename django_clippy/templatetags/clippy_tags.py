"""
clippy.py - clippy template tag
"""

from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()

last_clippy_id = 0

@register.filter
def clippy(text):
    """
    Generates a clippy html code

    param:
        text => text to generate the html code from

    """
    return mark_safe(render_to_string('clippy.html', {'text': text}).rstrip())
