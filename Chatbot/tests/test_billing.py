from app.billing import get_billing_info
import requests
from unittest.mock import patch

@patch('requests.get')
def test_get_billing_info(mock_get):
    mock_response = {
        "account_number": "12345",
        "balance": "2590.00",
        "due date": "2024-09-30"
    }
    mock_get.return_value.json.return_value = mock_response

    response = get_billing_info("12345")
    assert response['account_number'] == "12345"
    assert response['balance'] == "2590"
    assert response['due date'] == "2024-09-30"