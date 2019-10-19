from django.http import HttpResponse
from django.http import JsonResponse
import json


def get_txt_list(request):
    txt_list = {}
    text = json.loads(txt_list)

    return HttpResponse(text)


def show_article_list(request):
    if request.method == "GET":
        ll = [{'name': "图书", 'title': '测试数据'}]
        response = {'code': '200', 'msg': '查询成功', 'data': ll}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def show_list(request):
    return 0


def show_msg():
    return 0


def get_list():
    return 0
