from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils import simplejson


class MarkdownWidget(forms.Textarea):

    class Media:
        js = (
            (settings.STATIC_URL or settings.MEDIA_URL) + 'django_markdown/jquery.markitup.js',
            (settings.STATIC_URL or settings.MEDIA_URL) + 'django_markdown/markdown.js',
            settings.STATIC_URL + "django_markdown/auto_markdown.js",
        )
        css = {
            'screen': (
                (settings.STATIC_URL or settings.MEDIA_URL) + 'django_markdown/skins/%s/style.css' % getattr(settings, 'MARKDOWN_EDITOR_SKIN', 'markitup'),
                (settings.STATIC_URL or settings.MEDIA_URL) + 'django_markdown/markdown.css',
            )
        }

    def render(self, name, value, attrs=None):
        attrs = attrs or {}



        editor_settings = getattr(settings, 'MARKDOWN_EDITOR_SETTINGS', {})
        editor_settings['previewParserPath'] = reverse('django_markdown_preview')
        attrs["data-markdown-settings"] = simplejson.dumps(editor_settings);
        html = super(MarkdownWidget, self).render(name, value, attrs)

        return mark_safe(html)
