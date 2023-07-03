from django.shortcuts import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt


def home(request):
    rendered_page = render_to_string('index.html', {})
    return HttpResponse(rendered_page)