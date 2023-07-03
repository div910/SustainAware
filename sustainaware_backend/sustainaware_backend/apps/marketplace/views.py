from django.shortcuts import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from sustainaware_backend.apps.marketplace.dao import Dao
from sustainaware_backend.apps.marketplace.service import Recomender


def first(request):
    resp = Recomender().recomend_search_results({"filters": {"text": "shoes"}})
    print(resp)
    rendered_page = render_to_string('marketplace/index.html', resp)
    return HttpResponse(rendered_page)