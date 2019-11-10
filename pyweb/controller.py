from django.http import JsonResponse
from pyweb.models import AdminDb
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


def del_index_list(request):
    if request.method == "GET":
        response = {'code': '200', 'msg': '提交成功', 'data': request.GET.get("id")}
        logs.logs_on('获取数据')
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def get_admin(request):
    if request.method == "POST":
        list_data = AdminDb.objects.all()
        list_admin = []
        logs.logs_on("数据库 表tbl_admin_id 执行查操作")
        AdminDb.objects.order_by("tbl_admin_id")
        for var in list_data:
            dir_admin = {}
            dir_admin["name"] = var.name
            dir_admin["username"] = var.u_name
            dir_admin["password"] = var.p_word
            dir_admin["cTime"] = var.c_time
            list_admin.append(dir_admin)
        response = {'code': '200', 'msg': '提交成功', 'data': list_admin}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
    if request.method == "GET":
        logs.logs_on("发起了GET请求！")
        response = {'code': '400', 'msg': '请求参数有误，method = POST', 'data': 'error'}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
