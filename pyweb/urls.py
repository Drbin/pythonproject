from django.urls import path

from . import view
from . import controller

urlpatterns = [
    path('index/', view.index),
    path('index.html/', view.index),
    path('', view.index),
    path('get_list/', controller.get_txt_list),
    path('api/v1/show_article_list/', controller.show_article_list),
    path('exam/', view.exam),
    path('sure/', view.sure)

]

#handler404 = view.page_not_found
