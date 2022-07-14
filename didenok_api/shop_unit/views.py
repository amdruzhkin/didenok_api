import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def imports():
    pass

@csrf_exempt
def delete(uuid):
    pass

@csrf_exempt
def nodes(uuid):
    pass

@csrf_exempt
def sales():
    pass

@csrf_exempt
def node_statistic(uuid):
    pass
