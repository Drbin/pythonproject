from django.urls import path

from . import view

urlpatterns = [
    path('index/', view.index),
    path('index.html/', view.index),
    path('', view.index),
    path('exam/',view.exam),
    path('sure/', view.sure)

]
