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


def get_admin(request):
    if request.method == "POST":


        response = ""
        response1 = ""
        # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
        list = AdminDb.objects.all()

        logs.logs_on("数据库 表tbl_admin_id 执行查操作")
        AdminDb.objects.order_by("tbl_admin_id")

        # 输出所有数据
        for var in list:
            response1 += var.name + " "
        response = response1
        print(list)
        return HttpResponse("<p>" + response + "</p>")