from faker import Faker
from model_mommy.recipe import Recipe

from .models import ApplicationAddress

fake = Faker()

comment = Recipe(
    ApplicationAddress,
)
