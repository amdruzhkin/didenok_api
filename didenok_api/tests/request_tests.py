import json
import requests

host = "http://127.0.0.1:8000"

# 449d7dea-9332-46fe-944c-1377c2f6d39d
# 9caaec57-45d9-40f3-a5d8-0091fd4b5f50
# c1724bfa-0dbf-4336-b574-43c244720e0e
# c6beab3a-0f00-4b3c-9d98-d63bd3a477db


payload = {
    "items": [
        {
            "id": "9ae1e0ca-fe1a-464b-9471-15e41a52847a",
            "name": "Category 1",
            "date": "2022-05-28T21:12:01.000Z",
            "type": "CATEGORY",
        },
        {
            "id": "449d7dea-9332-46fe-944c-1377c2f6d39d",
            "name": "Category 2",
            "date": "2022-05-28T21:12:01.000Z",
            "type": "CATEGORY",
        },{
            "id": "bd122861-0d09-40ca-8241-0aa511057e26",
            "parentId": "9ae1e0ca-fe1a-464b-9471-15e41a52847a",
            "name": "Product 1",
            "date": "2022-05-28T21:12:01.000Z",
            "type": "OFFER",
            "price": 200,
        },{
            "id": "9be66d5b-cabc-4dc7-a1d0-fd54875660e4",
            "parentId": "449d7dea-9332-46fe-944c-1377c2f6d39d",
            "name": "Product 2",
            "date": "2022-05-28T21:12:01.000Z",
            "type": "OFFER",
            "price": 200,
        },{
            "id": "0cd4fa99-a05c-4728-982b-8c04c54f1ba0",
            "parentId": "449d7dea-9332-46fe-944c-1377c2f6d39d",
            "name": "Product 3",
            "date": "2022-05-28T21:12:01.000Z",
            "type": "OFFER",
            "price": 200,
        },{
            "id": "5861fe25-c9e0-44b0-a9be-2b49a36ff026",
            "parentId": "9ae1e0ca-fe1a-464b-9471-15e41a52847a",
            "name": "Product 4",
            "date": "2022-05-28T21:12:01.000Z",
            "type": "OFFER",
            "price": 200,
        },
    ]
}

# response = requests.post(host+"/imports", json=json.dumps(payload))
# print(response.text)

response = requests.delete(host+"/delete/9ae1e0ca-fe1a-464b-9471-15e41a52847a")
print(response.text)

# response = requests.get(host+"/nodes/9ae1e0ca-fe1a-464b-9471-15e41a52847a")
# print(response.text)

# response = requests.get(host+"/sales?date=2022-05-28T21%3A12%3A01.000Z")
# print(response.text)

# response = requests.get(host+"/node/37f1b9f1-404f-4e43-be42-b3cd28686a26/statistic?dateStart=2022-05-27T21%3A12%3A01.000Z&dateEnd=2022-05-29T21%3A12%3A01.000Z")
# print(response.text)