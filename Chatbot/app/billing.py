import requests

def get_billing_info(account_number):
    #Placeholder for billing API integration
    response = requests.get(f'https://billing-service/api/accounts/{account_number}')
    return response.json()