import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder

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
        if response["code"] == 200:
            return HttpResponse(status=response["code"], content=json.dumps(response["message"]))
        elif response["code"] == 404:
            return HttpResponse(status=response["code"],
                                content=json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))

@csrf_exempt
def sales(request):
    if request.method == "GET":
        response = ShopUnitController.on_sales(request.GET["date"])
        if response["code"] == 200:
            return HttpResponse(status=response["code"], content=json.dumps(response["message"]))
        elif response["code"] == 400:
            return HttpResponse(status=response["code"],
                                content=json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))

@csrf_exempt
def node_statistic(request, id):
    if request.method == "GET":
        date_from = None
        date_to = None
        response = {}
        try:
            date_from = request.GET["dateStart"]
        except Exception as e:
            pass
        try:
            date_to = request.GET["dateEnd"]
        except Exception as e:
            pass
        if date_from and date_to:
            response = ShopUnitController.on_node_statistic(id, date_from, date_to)
        elif date_from:
            response = ShopUnitController.on_node_statistic(id, date_form=date_from)
        elif date_to:
            response = ShopUnitController.on_node_statistic(id, date_to=date_to)
        else:
            response = ShopUnitController.on_node_statistic(id)

        if response["code"] == 200:
            return HttpResponse(status=response["code"], content=json.dumps(response["message"]))
        elif response["code"] == 400:
            return HttpResponse(status=response["code"],
                                content=json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
