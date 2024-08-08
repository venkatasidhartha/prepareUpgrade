import requests
import json

url = "http://127.0.0.1:8000/create_product"

for i in range(2,10000):
    payload = json.dumps({
    "name": f"laptop-{i}",
    "price": f"$ {40000*i}"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
