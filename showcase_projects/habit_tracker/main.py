import requests
import os
from datetime import datetime


def post():
    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    if response.status_code == 503:
        print("Rejected")
        post()
    else:
        print(response.text)


def put():
    response = requests.put(url=pixela_endpoint, json=pixel_params, headers=headers)
    if response.status_code == 503:
        print("Rejected")
        put()
    else:
        print(response.text)


USERNAME = "zacikmm"
TOKEN = os.environ.get("USER_TOKEN")
GRAPH_ID = "graph1"
DATE = datetime.today().strftime("%Y%m%d")
print(DATE)

pixela_endpoint = "https://pixe.la/v1/users"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "date": DATE,
    "quantity": "2.5",
}

pixel_params = {
    "quantity": "3"
}

put()

