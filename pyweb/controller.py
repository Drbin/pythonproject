from django.http import JsonResponse


def show_txt_msg(request):
    if request.method == "GET":
        ll = {'name': "图书", 'title': '测试数据'}
        response = {'code': '200', 'msg': '查询成功', 'data': ll}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def show_article_list(request):
    if request.method == "GET":
        ll = [{'name': "图书", 'title': '测试数据'}]
        response = {'code': '200', 'msg': '查询成功', 'data': ll}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def show_list(request):
    return 0


def show_msg():
    return 0


def get_list(request):
    if request.method == "GET":
        print(request.GET.get("id"))
        response = {'code': '200', 'msg': '提交成功', 'data': request.GET.get("id")}
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

