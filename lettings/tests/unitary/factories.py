"""
This file contains all the factories necessary to create fake instances of models for the tests
"""

import factory.fuzzy
from django.db import models
from lettings.models import Letting, Address


class AddressFactory(factory.django.DjangoModelFactory):
    """
    create fake instances of the Address model
    """
    number = factory.fuzzy.FuzzyInteger(low=1)
    street = factory.fuzzy.FuzzyText()
    city = factory.fuzzy.FuzzyText()
    state = factory.fuzzy.FuzzyText()
    zip_code = factory.fuzzy.FuzzyInteger(low=1, high=999999)
    country_iso_code = factory.fuzzy.FuzzyText(prefix="test_")

    class Meta:
        model = Address


class LettingFactory(factory.django.DjangoModelFactory):
    """
    create fake instances of the Letting model
    """
    id = factory.fuzzy.FuzzyInteger(low=1)
    title = factory.fuzzy.FuzzyText(prefix="test_")
    # SubFactory is used to replace the OneToOne link in models between letting and address
    address = factory.SubFactory(AddressFactory)
    class Meta:
        model = Letting
