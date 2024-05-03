from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    EMAIL_FIELD = 'email'
    photo = models.ImageField(upload_to='users/avatars/%Y/%m/%d/')

    def __str__(self):
        return self.get_full_name() + " " + str(self.id)

