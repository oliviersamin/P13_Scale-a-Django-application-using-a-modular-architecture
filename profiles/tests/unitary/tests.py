""" tests for views corresponding to profiles module"""
import pytest
from django.urls import reverse
from profiles.tests.unitary.factories import ProfileFactory


@pytest.mark.django_db
def test_index(client):
    url = reverse('profiles:index')
    response = client.get(url)
    data = response.content.decode()
    expected_title = "<h1>Profiles</h1>"
    assert response.status_code == 200
    assert expected_title in data


@pytest.mark.django_db
def test_profile(client):
    """
    Usage of the ProfileFactory class created in factories.py (source = "Django crash course")
    It create a fake instance of the desired model to be able to perform a QuerySet
    """

    test_profile = ProfileFactory()
    url = reverse('profiles:profile', args=[test_profile.user.username])
    response = client.get(url)
    data = response.content.decode()
    expected_title = "<title>{}</title>".format(test_profile.user.username)
    assert response.status_code == 200
    assert expected_title in data
