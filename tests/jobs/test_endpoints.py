def test_get_job(client):
    response = client.get('/jobs')

    assert b'Hello /jobs' == response.data
    assert response.status_code == 200


def test_create_job(client):
    post_data = {'foo': 'bar'}
    response = client.post('/create_job', json=post_data)

    assert b'Job created' in response.data
    assert response.status_code == 200
