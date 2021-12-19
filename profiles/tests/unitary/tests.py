""" tests for views corresponding to profiles module"""
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    url = reverse('profiles:index')
    response = client.get(url)
    data = response.content.decode()
    expected_title = "<h1>Profiles</h1>"
    assert response.status_code == 200
    assert expected_title in data
