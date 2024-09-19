from app import create_app

app = create_app()
client = app.test_client()

def test_access_token():
    response = client.get('/oauth/token')
    assert response.status_code == 200
    data = response.get_json()
    assert 'token' in data