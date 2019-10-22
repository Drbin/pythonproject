from django.http import JsonResponse
from . import logs


def show_txt_msg(request):
    if request.method == "GET":
        ll = {'name': "图书", 'title': '测试数据'}
        response = {'code': '200', 'msg': '查询成功', 'data': ll}
        logs.logs_on('查询数据')
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def show_article_list(request):
    if request.method == "GET":
        ll = [{'name': "图书", 'title': '测试数据'}]
        response = {'code': '200', 'msg': '查询成功', 'data': ll}
        logs.logs_on('查询数据')
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def get_list(request):
    if request.method == "GET":
        print(request.GET.get("id"))
        response = {'code': '200', 'msg': '提交成功', 'data': request.GET.get("id")}
        logs.logs_on('获取数据')
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

