# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def preview(request):
    media_or_static = settings.STATIC_URL or settings.MEDIA_URL
    css = getattr(settings, 'DJANGO_MARKDOWN_STYLE', media_or_static + 'django_markdown/preview.css')
    # prise en compte de plusieurs style, et retrocompatibilité avec l'anciens mode
    if not isinstance(css, (list, tuple)):
        css_files = (css,)
    else:
        css_files = css

    return render(
        request, 'django_markdown/preview.html',
        {'content':request.REQUEST.get('data', 'No content posted'), 'css_files':css_files})
