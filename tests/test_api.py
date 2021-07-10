import pytest
@pytest.fixture
def client():
    from app import app
    return app.test_client()
def test_health(client):
    assert client.get('/health').status_code == 200