import json
import pytest
import requests


class TestImports:
    host = "http://127.0.0.1:8000"
    payload_tests = [
        ({"items": [
                {"id": "3fa85f64-5717-4562-b3fc-2c963f66a333",
                "name": "product_1",
                "date": "2022-05-28T21:12:01.000Z",
                "type": "OFFER"},
            ]
         }, 200),
        ({"items": [
            {"id": "3fa85f64-!@#$-4562-b3fc-2c963f66a333",  # Invalid UUID format
             "name": "product_1",
             "date": "2022-05-28T21:12:01.000Z",
             "type": "OFFER"},
        ]
         }, 400),
        ({"items": [
            {"id": "3fa85f64-!@#$-4562-b3fc-2c963f66a333",
             # "name": "product_1",  # Missing Required Fields
             "date": "2022-05-28T21:12:01.000Z",
             "type": "OFFER"},
        ]
         }, 400),
        ({"items": [
            {"id": "3fa85f64-!@#$-4562-b3fc-2c963f66a333",
             "name": "product_1",
             "date": "2022/05/28T21:12:01.000Z", # Invalid Date Format
             "type": "OFFER"},
        ]
         }, 400),
        ({"items": [
            {"id": "3fa85f64-!@#$-4562-b3fc-2c963f66a333",
             "name": "product_1",
             "date": "2022/05/28T21:12:01.000Z",
             "type": "PRODUCT"},  # Invalid Type
        ]
         }, 400),
    ]

    @pytest.mark.parametrize('payload, code', payload_tests)
    def test_imports(self, payload, code):
        endpoint = "/imports"
        url = self.host + endpoint
        response = requests.post(url, json=json.dumps(payload))
        assert response.status_code == code, response.text