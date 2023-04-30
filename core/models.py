from django.db import models
from django.contrib.auth.models import AbstractUser


class UserApp(AbstractUser):

    # is_admin = models.BooleanField(default=False, blank=False)
    # is_manager = models.BooleanField(default=False, blank=False)
    # is_searcher = models.BooleanField(default=False, blank=False)
    # is_student = models.BooleanField(default=True, blank=False)
    phone = models.CharField(max_length=50, null=True, blank=True)
    date_birth = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    role = models.CharField(max_length=10, null=True, blank=True)


class Etudiant(UserApp):
    test = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=10, null=True,
                            blank=True, default='Etudient')
