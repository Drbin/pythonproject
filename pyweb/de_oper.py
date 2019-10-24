from django.http import HttpResponse

from pyweb.models import InitDb


# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = InitDb.objects.all()

    InitDb.objects.order_by("id")

    # 上面的方法可以连锁使用
    InitDb.objects.filter(name="admin_tbl").order_by("tbl_admin_id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
