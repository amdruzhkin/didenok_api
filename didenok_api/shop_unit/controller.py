import json

from shop_unit.models import ShopUnit


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
        return {"code": 200, "message": id}

    @staticmethod
    def on_nodes(id):
        return {"code": 200, "message": id}

    @staticmethod
    def on_sales(date):
        return {"code": 200, "message": date}

    @staticmethod
    def on_node_statistic(id, date_form=None, date_to=None):
        return {"code": 200, "message": {"id": id, "date_form": date_form, "date_to": date_to}}

