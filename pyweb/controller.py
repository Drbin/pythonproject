from django.http import HttpResponse
import json


def get_txt_list(request):
    txt_list = {}
    text = json.loads(txt_list)

    return HttpResponse(text)


def show_list(request):
    return 0


def show_msg():
    return 0


def get_list():
    return 0
