import json

class ShopUnitController:
    @staticmethod
    def on_import(payload):
        return {"code": 200, "message": "Success import"}
        # data = json.loads(payload)
        # if not data["items"] or len(data["items"]) == 0:
        #     return {"code": 400, "message": "Validation Failed"}

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

