from pyweb.models import AdminDb
from . import logs


def re_admin_data():
    list = AdminDb.objects.all()
    list_admin = []
    logs.logs_on("数据库 表tbl_admin_id 执行查操作")
    AdminDb.objects.order_by("tbl_admin_id")

    # 输出所有数据
    for var in list:
        dir_admin = {}
        dir_admin["name"] = var.name
        dir_admin["username"] = var.u_name
        dir_admin["password"] = var.p_word
        dir_admin["cTime"] = var.c_time
        list_admin.append(dir_admin)
    return list_admin

