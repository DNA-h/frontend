from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel

class User(AbstractUser, TimeStampedModel):
    pass
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-created',)


    def __str__(self):
        # return self.first_name + " " + self.last_name
        return self.email