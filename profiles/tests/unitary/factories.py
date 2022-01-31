"""
This file contains all the factories necessary to create fake instances of models for the tests
"""

import factory.fuzzy
from profiles.models import Profile
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """
    create a fake instance of the User model
    """
    username = factory.fuzzy.FuzzyText()

    class Meta:
        model = User


class ProfileFactory(factory.django.DjangoModelFactory):
    """
    create fake instances of the Profile model
    """
    user = factory.fuzzy.FuzzyInteger(low=1)
    # SubFactory is used to replace the OneToOne link in models between Profile and User
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Profile
