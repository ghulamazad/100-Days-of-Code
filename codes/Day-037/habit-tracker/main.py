import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "ddbfh4r4h574bvhbc"
USERNAME = "ghulam"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)


PIXELA_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=2, day=5)

pixela_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km did you run today? ")
}

response = requests.post(url=PIXELA_CREATION_ENDPOINT, json=pixela_data, headers=headers)
print(response.text)

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixela_data = {
    "quantity": "2.3"
}
# response = requests.put(url=UPDATE_ENDPOINT, json=new_pixela_data, headers=headers)
# print(response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)
