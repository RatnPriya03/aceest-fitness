from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the root endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to ACEest_Fitness!" in response.data

def test_members_api_endpoint(client):
    """Test the /api/members endpoint."""
    response = client.get('/api/members')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    members = response.get_json()
    assert isinstance(members, list)
    assert len(members) > 0
    assert "John Doe" in members[0]['name']