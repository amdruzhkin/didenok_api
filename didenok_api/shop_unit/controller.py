import json
from datetime import datetime, timedelta

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
            unit["children"] = ShopUnitController._get_childrens(query.id, query.type)

            ShopUnitController._count_price(unit)
            ShopUnitController._count_price(unit)  # Fast solution

            return {"code": 200, "message": unit}
        except ObjectDoesNotExist as e:
            return {"code": 404, "message": "Item not found"}
        except ValidationError as e:
            return {"code": 400, "message": "Validation Failed"}

    @staticmethod
    def _get_childrens(id, type):
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
            children["children"] = ShopUnitController._get_childrens(q.id, q.type)
            childrens.append(children)
        return childrens

    @staticmethod
    def _count_price(unit):
        if not unit["children"] or unit["children"] is None:
            return
        unit["price"] = 0
        for c in unit["children"]:
            unit["price"] += c["price"] if isinstance(c["price"], int) else 0
            ShopUnitController._count_price(c)
        if unit["price"] == 0:
            unit["price"] = None


    @staticmethod
    def on_sales(date):
        try:
            Validator.check_date(date)
            date_from = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z') - timedelta(days=1)
            date_from = date_from.isoformat()[:-6] + ".000Z"
            date_to = date

            query = ShopUnit.objects.filter(type="OFFER", date__gte=date_from, date__lte=date_to)
            items = []
            for q in query:
                item = model_to_dict(q)
                item["date"] = str(item["date"])
                items.append(item)

            return {"code": 200, "message": {"items": items}}
        except ValidationError as e:
            return {"code": 400, "message": "Validation Failed"}

    @staticmethod
    def on_node_statistic(id, date_form=None, date_to=None):
        try:
            Validator.check_uuid(id)
            if date_form:
                Validator.check_date(date_form)
            if date_to:
                Validator.check_date(date_to)

            try:
                query = None

                if date_form and date_to:
                    query = ShopUnit.objects.get(pk=id, date__gte=date_form, date__lte=date_to)
                elif date_form:
                    query = ShopUnit.objects.get(pk=id, date__gte=date_form)
                elif date_to:
                    query = ShopUnit.objects.get(pk=id, date__lte=date_to)
                else:
                    query = ShopUnit.objects.get(pk=id)

                unit = model_to_dict(query)
                unit["date"] = str(unit["date"])
                unit["children"] = ShopUnitController._get_childrens(query.id, query.type)

                ShopUnitController._count_avg(unit)
                ShopUnitController._count_avg(unit)  # Fast solution

                return {"code": 200, "message": unit}
            except ObjectDoesNotExist as e:
                return {"code": 404, "message": "Item not found"}

        except ValidationError as e:
            return {"code": 400, "message": "Validation Failed"}

    @staticmethod
    def _count_avg(unit):
        if not unit["children"] or unit["children"] is None:
            return
        unit["price"] = 0
        for c in unit["children"]:
            unit["price"] += c["price"] if c["price"] is not None else 0
            ShopUnitController._count_avg(c)
        unit["price"] = unit["price"] / len(unit["children"])
        print("DIVIDED", unit["price"])
        if unit["price"] == 0:
            unit["price"] = None

