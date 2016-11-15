from uuid import uuid4

from django.conf import settings


def get_user_uid(request):
    return request.COOKIES.get(settings.USER_UID_COOKIE_KEY)


def make_user_uid(request):
    return uuid4().hex


def set_user_uid_cookie(response, cookie_value):
    response.set_cookie(settings.USER_UID_COOKIE_KEY, cookie_value, max_age=365 * 24 * 60 * 60)
    return response