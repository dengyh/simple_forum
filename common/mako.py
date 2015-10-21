# -*- coding: utf-8 -*-

from mako.lookup import TemplateLookup
from django.conf import settings
from django.http import HttpResponse
from django.template import Context, RequestContext

lookup = TemplateLookup(
    directories=settings.MAKO_TEMPLATE_DIR,
    module_directory=settings.MAKO_TEMPLATE_MODULE_DIR,
    output_encoding='utf-8',
    input_encoding='utf-8',
    encoding_errors='replace',
    collection_size=500,
)

def render(request, templateName, dictionary={}):
    contextInstance = RequestContext(request)
    template = lookup.get_template(templateName)

    if contextInstance:
        contextInstance.update(dictionary)
    else:
        contextInstance = Context(dictionary)

    data = {}
    for d in contextInstance:
        data.update(d)

    return HttpResponse(template.render_unicode(**data))
