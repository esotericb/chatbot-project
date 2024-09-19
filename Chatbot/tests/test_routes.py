import json
from app import create_app

app = create_app()

def test_chat_route():
    client = app.test_client()
    data = {"query": "What is my bill amount?"}
    response = client.post('/chat', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert "bill" in response_data['response']
