import requests
import json

#GET
status='available'


status='available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())

#POST

url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Котик"
  },
  "name": "Агат",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "Съеден"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

#PUT
url1 = "https://petstore.swagger.io/v2/pet"

headers = {
    'accept': 'application/json',
    'auth_key': 'key',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Кошка"
  },
  "name": "Агата",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.put(url1, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
dict = response.json()

# DELETE
pet_id = dict.get("id")
url2 = f"https://petstore.swagger.io/v2/pet/{pet_id}"
response = requests.delete(url2)
print(response.status_code)
print(response.text)
