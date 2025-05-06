import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "users_django.settings")
django.setup()

from users.models import User

user = User(name = "Данило", email="danylo.com@gmail.com")

user.save()

