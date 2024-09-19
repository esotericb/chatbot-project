import requests

CRM_API_BASE_URL = "https://crm-service/api"

def get_customer_details(customer_id):
    try:
        response = requests.get(f'{CRM_API_BASE_URL}/customers/{customer_id}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def update_customer_details(customer_id, data):
    try:
        response = requets.put(f'{CRM_API_BASE_URL}/customers/{customer_id}', json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}