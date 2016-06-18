def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Hello world!' in response.data.decode()
