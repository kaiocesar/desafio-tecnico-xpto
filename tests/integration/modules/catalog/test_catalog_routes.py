

def test_get_awards(client):
    response = client.get("/api/v1/catalog/awards")
    assert response.status_code == 200
    assert response.json() == {"min": [], "max": []}
