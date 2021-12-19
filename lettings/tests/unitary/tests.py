""" tests for views corresponding to lettings module"""
import pytest
from django.urls import reverse
from lettings.models import Letting

@pytest.mark.django_db(transaction=True)
def test_index(client):
    url = reverse('lettings:index')
    response = client.get(url)
    data = response.content.decode()
    expected_title = "<h1>Lettings</h1>"
    assert response.status_code == 200
    assert expected_title in data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_letting(client):
    # url = reverse('lettings:letting', args=[2])
    # response = client.get(url)
    test = Letting.objects.all()
    print("\n########################\n")
    print(test)
    # data = response.content.decode()
    # print("\n#########  DATA LETTING WITH ARG ##########\n")
    # print(data)
    # print("\n######################")
    # expected_title = "Oceanview Retreat"
    # assert response.status_code == 200
    # assert expected_title in data
