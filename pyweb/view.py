from django.shortcuts import render
from django.shortcuts import render_to_response


def index(request):
    return render(request, 'index.html')


def exam(request):
    return render(request, 'exam.html')


def sure(request):
    return render(request, 'sure.html')


def page_not_found(request, **kwargs):
    response = render_to_response('404.html', {})
    response.status_code = 400
    return response


def run():
    return
