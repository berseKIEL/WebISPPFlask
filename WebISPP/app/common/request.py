import requests

def get_request_json(url):
    response = requests.get(url)
    if (response.status_code == 200):
        return response
    elif (response.status_code == 404):
        return 'Recurso no encontrado'

def get_request_queried_json(url,data):
    response = requests.get(url,params=data)
    if (response.status_code == 200):
        return response
    elif (response.status_code == 404):
        return 'Recurso no encontrado'
    
def post_request_json(url, data):
    response = requests.post(url,data=data)
    if (response.status_code == 200):
        return response
    elif (response.status_code == 404):
        return 'Recurso no encontrado'

def update_request_json(url,data):
    response = requests.put(url,data=data)
    if (response.status_code == 200):
        return response
    elif (response.status_code == 404):
        return 'Recurso no encontrado'