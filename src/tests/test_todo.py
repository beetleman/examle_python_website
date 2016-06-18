def test_todo_get(client):
    response = client.get('/todo/')
    assert response.status_code == 200
    assert 'TODO:' in response.data.decode()


def test_todo_post(client):
    new_item = 'noooopeee'
    response = client.post('/todo/',  data=dict(
        text=new_item,
    ), follow_redirects=True)
    assert response.status_code == 200
    assert '<li>{}</li>'.format(new_item) in response.data.decode()
