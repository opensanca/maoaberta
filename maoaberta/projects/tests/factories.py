import factory
from projects.models import Project
from contributors.tests.factories import UserFactory


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = factory.Faker("catch_phrase")
    date = factory.Faker("date", locale="pt_BR")
    description = factory.Faker("text", locale="pt_BR")
    status = 'open'
    responsible = factory.SubFactory(UserFactory)
