import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}