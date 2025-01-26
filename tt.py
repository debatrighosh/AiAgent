import json
import requests

api_url = 'https://gorest.co.in/public/v2/users'
access_token = '7eadfeb0a788676c82a15b9870346efb930a4fa5069897cf0bfa01b0ee92c074'  # Replace with your actual token

# Headers with authentication
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response=requests.post(api_url,headers=headers);
if response.status_code == 200:
    data_lst = json.loads(response.content.decode());
    print(data_lst);
return response.json()
else:
    return []
a=response.text;

data_lst = json.loads(response.content.decode());
print(data_lst);


def filter_users(users):
    """
    Filters users based on gender 'female' and status 'inactive'.

    Args:
        users (list): A list of dictionaries, where each dictionary represents a user.

    Returns:
        str: A JSON array of filtered users.
    """
    filtered_users = [user for user in users if user.get("gender") == "female" and user.get("status") == "inactive"]
    return json.dumps(filtered_users, indent=4)

users_list = [
    {"id": 1, "name": "Alice", "gender": "female", "status": "active"},
    {"id": 2, "name": "Betty", "gender": "female", "status": "inactive"},
    {"id": 3, "name": "Charlie", "gender": "male", "status": "inactive"},
    {"id": 4, "name": "Diana", "gender": "female", "status": "inactive"},
]

result = filter_users(users_list)
print(result)