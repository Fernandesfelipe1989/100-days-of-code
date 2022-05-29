import datetime as dt
import requests

from decouple import config
# BASE_URL = 'https://pixe.la'
BASE_URL = config('PIXELA_BASE_URL')
USERNAME = config('PIXELA_USERNAME')
TOKEN = config('PIXELA_TOKEN')

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url=BASE_URL, json=user_params)


# GRAPH_ENDPOINT = f'{BASE_URL}/{USERNAME}/graphs'
#
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# graphs_params = {
#     'id': 'graph1',
#     'name': 'Cycling Graph',
#     'unit': 'Km',
#     'type': "float",
#     'color': 'ajisai',
# }
# response = requests.post(url=GRAPH_ENDPOINT, json=graphs_params, headers=headers)
qty = 50
GRAPHS_ID = 'graph1'
# GRAPH_ENDPOINT = f'{BASE_URL}/{USERNAME}/graphs/{GRAPHS_ID}'
headers = {
    'X-USER-TOKEN': TOKEN
}
day = dt.datetime.today() - dt.timedelta(days=0)
day = day.strftime("%Y%m%d")
# data_graph_parameters = {
#     'date': day,
#     'quantity': str(qty),
# }
# response = requests.post(url=GRAPH_ENDPOINT, json=data_graph_parameters, headers=headers)
# print(response.text)
GRAPH_ENDPOINT = f'{BASE_URL}/{USERNAME}/graphs/{GRAPHS_ID}/{day}'
# data_graph_parameters = {
#     'quantity': str(qty),
# }
# response = requests.put(url=GRAPH_ENDPOINT, json=data_graph_parameters, headers=headers)
response = requests.delete(url=GRAPH_ENDPOINT, headers=headers)
print(response.text)
