from django.shortcuts import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from sustainaware_backend.apps.profile.dao import Dao
def login(requests):

    get_body = requests.GET
    login_success = False
    rendered_page = render_to_string('profile/login.html', {})
    if 'username' not in get_body or 'password' not in get_body:
        return HttpResponse(rendered_page)
    user_row = Dao().get_account_by_username(username=get_body.get('username'))
    if get_body.get('password') == user_row[0].get('password'):
        login_success = True

    if login_success is True:
        rendered_page = render_to_string('profile/index.html', user_row[0])
        return HttpResponse(rendered_page)
    else:
        rendered_page = render_to_string('profile/login.html', {})
        return HttpResponse(rendered_page)

def first(request):
    rendered_page = render_to_string('profile/index.html', {})
    return HttpResponse(rendered_page)