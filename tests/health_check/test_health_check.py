def test_read_main(client):
    """
    Test the /status endpoint.
    Ensures that the health check endpoint returns status 200.
    """
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
