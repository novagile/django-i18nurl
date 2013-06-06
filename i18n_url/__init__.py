# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils import translation


def reverse_i18n(url, language, *args, **kwargs):
    """Return the i18n url in a specific language."""
    cur_language = translation.get_language()
    try:
        translation.activate(language)
        url = reverse(url, *args, **kwargs)
    finally:
        translation.activate(cur_language)
    return url
