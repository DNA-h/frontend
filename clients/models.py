from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel
from django.db import models


class User(AbstractUser, TimeStampedModel):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-created',)


    def __str__(self):
        # return self.first_name + " " + self.last_name
        return self.email
