# Django
from django.db import IntegrityError
from django.core.management import BaseCommand
from django.contrib.auth.hashers import make_password

# Python
from faker import Faker
import string
import random


# Local
from auths.models import MyCustomUser


fake = Faker("ru_RU")

class Command(BaseCommand):
    """Command for generate data for Database."""

    def generate_password(self, length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def create_users(self):
        for _ in range(1_000_000):
                name: str = fake.first_name()
                email: str = fake.ascii_free_email()
                phone_number: str = fake.phone_number()
                password: str = self.generate_password()
                try:
                        MyCustomUser.objects.create_user(
                                username=name,
                                email=email,
                                phone_number=phone_number,
                                password=password
                        )
                except IntegrityError:
                        print(f'User {name} already exists!')

    def handle(self, *args, **kwargs):
        self.create_users()
        print("FINISH")


