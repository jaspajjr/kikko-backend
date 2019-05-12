def test_get_job(client):
    response = client.get('/jobs')

    assert b'Hello /jobs' == response.data
    assert response.status_code == 200
