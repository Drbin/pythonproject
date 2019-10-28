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
        response = {'code': '200', 'msg': '提交成功', 'data': request.GET.get("id")}
        logs.logs_on('获取数据')
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def get_admin(request):
    if request.method == "POST":
        from . import mapper

        # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
        list_admin = mapper.re_admin_data

        response = {'code': '200', 'msg': '提交成功', 'data': list_admin}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
    if request == "GET":
        response = {'code': 'error', 'msg': '请求参数有误，method = POST'}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
