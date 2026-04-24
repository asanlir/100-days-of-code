import requests
from datetime import datetime

USERNAME = "this_is_a_test_username"
TOKEN = "this_is_a_test_token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create a new user account
response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Create a new graph
graph_params = {
    "id": "graph1",
    "name": "Graph 1",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN  
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# Add a pixel to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many commits did you make today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# Update a pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
updated_pixel_data = {
    "quantity": "10"
}

response = requests.put(url=pixel_update_endpoint, json=updated_pixel_data, headers=headers)

# Delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=pixel_delete_endpoint, headers=headers)
