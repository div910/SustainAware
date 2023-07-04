from django.shortcuts import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from sustainaware_backend.apps.recycle_wizard.dao import Dao
def add_post(requests):
    username = requests.GET.get("username")
    post = requests.GET.get("post")
    Dao().add_posts_by_username(username, post)
    rendered_page = render_to_string('recycle_wizard/index.html', {})
    return HttpResponse(rendered_page)

def get_post(requests):
    username = requests.GET.get("username")
    posts = []
    if username is not None:
        posts = Dao().get_posts_by_username(username)

    posts = posts if posts is not None else []
    rendered_page = render_to_string('recycle_wizard/index.html', posts)
    return HttpResponse(rendered_page)

def first(request):
    rendered_page = render_to_string('recycle_wizard/index.html', {})
    return HttpResponse(rendered_page)