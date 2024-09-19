from app.crm import get_customer_details
import requests
from unittest.mock import patch

@patch('requests.get')
def test_get_customer_details(mock_get):
    mock_response = {
        "customer_id": "1",
        "name": "John Doe",
        "address": "123 Main St"
    }

    response = get_customer_details("1")
    assert response ['customer id'] == "1"
    assert response['name'] == "John Doe"
    assert response['address'] == "123 Main St"