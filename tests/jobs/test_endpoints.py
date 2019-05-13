def test_get_job(client):
    response = client.get('/jobs')

    assert b'Hello /jobs' == response.data
    assert response.status_code == 200


def test_create_job(client):
    post_data = {
        "job": {
            "ids": 23,
            "contact_email": "tom@example.com",
            "password": "foobar",
            "company_name": "Acme",
            "job_title": "FE Developer",
            "job_description": "Do FE Development",
            "location": "Manchester",
            "salary_min": 30000,
            "salary_max": 50000
            }}

    response = client.post('/create_job', json=post_data)

    assert b'Job created' in response.data
    assert response.status_code == 200
