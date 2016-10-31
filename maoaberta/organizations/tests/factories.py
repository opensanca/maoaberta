import factory

from organizations.models import Organization, Necessity
from projects.tests.factories import ProjectFactory
from contributors.tests.factories import ContributorFactory


class NecessityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Necessity

    name = factory.Faker("name", locale="pt_BR")
    satisfied = False


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Faker("company", locale="pt_BR")

    description = factory.Faker("text")

    coordinator = factory.SubFactory(ContributorFactory)

    #projects = factory.SubFactory(ProjectFactory)

    #necessities = factory.SubFactory(NecessityFactory)

    necessity_description = factory.Faker("text")

    email = factory.Faker("email", locale="pt_BR")

    homepage_url = "http://rotaract.org/"

    facebook_url = "http://facebook.com/"

    twitter_url = "http://twitter.com/"
