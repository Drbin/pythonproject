from django.urls import path

from . import view
from . import controller

urlpatterns = [
    path('index/', view.index),
    path('index.html/', view.index),
    path('', view.index),
    path('api/v1/show_txt_msg/', controller.show_txt_msg),
    path('api/v1/show_article_list/', controller.show_article_list),
    path('api/v1/getList/', controller.get_list),
    path('exam/', view.exam),
    path('sure/', view.sure),
    path('api/v1/getAdmin/', controller.get_admin),
    path('api/v1/delAdmin/', controller.del_admin_item)

]

#handler404 = view.page_not_found
