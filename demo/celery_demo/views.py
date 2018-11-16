from django.http import JsonResponse
from django.shortcuts import render

from celery_demo.tasks import DemoTask


def do(request):
    print('start do')
    # DemoTask.delay()
    DemoTask.apply_async(args=('hello',), queue='work')
    print('end do')
    return JsonResponse({'result': 'ok'})

