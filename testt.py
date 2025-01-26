import json
import requests


api_url = 'https://gorest.co.in/public/v2/users'
access_token = '7eadfeb0a788676c82a15b9870346efb930a4fa5069897cf0bfa01b0ee92c074'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.post(api_url, headers=headers).json
print(response)


users_list = [
    {"id": 1, "name": "Alice", "gender": "female", "status": "active"},
    {"id": 2, "name": "Betty", "gender": "female", "status": "inactive"},
    {"id": 3, "name": "Charlie", "gender": "male", "status": "inactive"},
    {"id": 4, "name": "Diana", "gender": "female", "status": "inactive"},
]

