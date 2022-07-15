import json
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms.models import model_to_dict

from shop_unit.models import ShopUnit
from shop_unit.validator import Validator


class ShopUnitController:
    @staticmethod
    def on_import(payload):
        data = None
        if type(payload) == bytes:
            data = json.loads(payload)
            data = json.loads(data)

        if not data["items"] or len(data["items"]) == 0:
            return {"code": 400, "message": "Validation Failed"}

        try:
            for item in data["items"]:
                try:
                    new_item = ShopUnit()
                    new_item.__dict__.update(item)
                    new_item.save()
                except Exception as e:
                    return {"code": 400, "message": "Validation Failed"}

            return {"code": 200, "message": "Success Import"}
        except Exception as e:
            return {"code": 400, "message": "Validation Failed"}


    @staticmethod
    def on_delete(id):
        try:
            Validator.check_uuid(id)
            ShopUnit.objects.get(pk=id).delete()
            return {"code": 200, "message": "Success delete"}
        except ObjectDoesNotExist as e:
            return {"code": 404, "message": "Item not found"}
        except ValidationError as e:
            return {"code": 400, "message": "Validation Failed"}


    @staticmethod
    def on_nodes(id):
        try:
            Validator.check_uuid(id)
            query = ShopUnit.objects.get(pk=id)
            unit = model_to_dict(query)
            unit["date"] = str(unit["date"])
            unit["children"] = ShopUnitController.get_childrens(query.id, query.type)

            ShopUnitController.count_price(unit)
            ShopUnitController.count_price(unit)  # Fast solution

            return {"code": 200, "message": unit}
        except ObjectDoesNotExist as e:
            return {"code": 404, "message": "Item not found"}
        except ValidationError as e:
            return {"code": 400, "message": "Validation Failed"}

    @staticmethod
    def get_childrens(id, type):
        childrens = []
        query = ShopUnit.objects.filter(parentId=id)
        if len(query) == 0:
            if type == "OFFER":
                return None
            elif type == "CATEGORY":
                return []
        for q in query:
            children = model_to_dict(q)
            children["date"] = str(children["date"])
            children["children"] = ShopUnitController.get_childrens(q.id, q.type)
            childrens.append(children)
        return childrens

    @staticmethod
    def count_price(unit):
        if not unit["children"] or unit["children"] is None:
            return
        unit["price"] = 0
        for c in unit["children"]:
            unit["price"] += c["price"] if isinstance(c["price"], int) else 0
            ShopUnitController.count_price(c)
        if unit["price"] == 0:
            unit["price"] = None


    @staticmethod
    def on_sales(date):
        return {"code": 200, "message": date}

    @staticmethod
    def on_node_statistic(id, date_form=None, date_to=None):
        return {"code": 200, "message": {"id": id, "date_form": date_form, "date_to": date_to}}

