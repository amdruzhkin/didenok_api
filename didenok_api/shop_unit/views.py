import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from shop_unit.controller import ShopUnitController


@csrf_exempt
def imports(request):
    if request.method == "POST":
        response = ShopUnitController.on_import(request.body)
        return HttpResponse(status=response["code"], content=json.dumps(response))

@csrf_exempt
def delete(request, id):
    if request.method == "DELETE":
        response = ShopUnitController.on_delete(id)
        return HttpResponse(status=response["code"], content=json.dumps(response))

@csrf_exempt
def nodes(request, id):
    if request.method == "GET":
        response = ShopUnitController.on_nodes(id)
        return HttpResponse(status=response["code"], content=json.dumps(response))

@csrf_exempt
def sales(request):
    if request.method == "GET":
        response = ShopUnitController.on_sales(request.GET["date"])
        return HttpResponse(status=response["code"], content=json.dumps(response))

@csrf_exempt
def node_statistic(request, id):
    if request.method == "GET":
        response = ShopUnitController.on_node_statistic(id, request.GET["dateStart"], request.GET["dateEnd"])
        return HttpResponse(status=response["code"], content=json.dumps(response))
