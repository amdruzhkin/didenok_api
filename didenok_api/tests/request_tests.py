import json
import requests

host = "http://127.0.0.1:8000"

# response = requests.post(host+"/imports", json=json.dumps({"key": "value"}))
# print(response.text)

# response = requests.delete(host+"/delete/9ae1e0ca-fe1a-464b-9471-15e41a52847a")
# print(response.text)

# response = requests.get(host+"/nodes/9ae1e0ca-fe1a-464b-9471-15e41a52847a")
# print(response.text)

# response = requests.get(host+"/sales?date=2022-05-28T21%3A12%3A01.000Z")
# print(response.text)

response = requests.get(host+"/node/37f1b9f1-404f-4e43-be42-b3cd28686a26/statistic?dateStart=2022-05-27T21%3A12%3A01.000Z&dateEnd=2022-05-29T21%3A12%3A01.000Z")
print(response.text)