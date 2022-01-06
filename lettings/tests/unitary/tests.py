""" tests for views corresponding to lettings module"""
import pytest
from django.urls import reverse
from lettings.tests.unitary.factories import LettingFactory


@pytest.mark.django_db
def test_index(client):
    url = reverse('lettings:index')
    response = client.get(url)
    data = response.content.decode()
    expected_title = "<h1>Lettings</h1>"
#    assert response.status_code == 200
    assert expected_title in data


@pytest.mark.django_db
def test_letting(client):
    """
    Usage of the LettingFactory class created in factories.py (source = "Django crash course")
    It create a fake instance of the desired model to be able to perform a QuerySet
    """

    test_letting = LettingFactory()
    url = reverse('lettings:letting', args=[test_letting.id])
    response = client.get(url)
    data = response.content.decode()
    expected_title = "<title>{}</title>".format(test_letting.title)
#    assert response.status_code == 200
    assert expected_title in data
