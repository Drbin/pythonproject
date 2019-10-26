from django.http import HttpResponse

from pyweb.models import AdminDb

def testdb(request):
    # 初始化
    response = ""
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = AdminDb.objects.all()

    AdminDb.objects.order_by("tbl_admin_id")
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    print(list)
    return HttpResponse("<p>" + response + "</p>")
