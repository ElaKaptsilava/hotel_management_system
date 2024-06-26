import factory
from hotel_management.factories import UserFactory
from reviews.models import AbstractReview


class AbstractReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AbstractReview

    pk = factory.Sequence(lambda n: n)
    user = factory.SubFactory(UserFactory)  # Assuming you have a UserFactory defined
    rate = factory.Faker("random_int", min=1, max=5)
    title = factory.Faker("sentence", nb_words=6)
    comment = factory.Faker("paragraph", nb_sentences=3)
