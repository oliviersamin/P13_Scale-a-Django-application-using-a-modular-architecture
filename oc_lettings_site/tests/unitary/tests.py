""" tests for views corresponding to oc_lettings_site module"""
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    url = reverse('index')
    response = client.get(url)
    data = response.content.decode()
    expected_title = "<h1>Welcome to Holiday Homes</h1>"
#    assert response.status_code == 200
    assert expected_title in data
