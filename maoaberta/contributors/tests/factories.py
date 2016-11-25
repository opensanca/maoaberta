from django.contrib.auth.models import User

import factory

from contributors.models import Contributor


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username", )

    username = factory.Sequence(lambda n: 'george%s' % n)
    first_name = factory.Faker("first_name", locale="pt_BR")
    last_name = factory.Faker("last_name", locale="pt_BR")
    email = factory.Faker("email", locale="pt_BR")
    password = "senhamuitoforte"


class ContributorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contributor

    user = factory.SubFactory(UserFactory)
