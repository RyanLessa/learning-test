from django.db import models
from django.contrib.auth.models import User as BaseUser


class User(BaseUser):
    """This model is responsible for representate a user authenticated in
    the system"""
    name = models.CharField(u'Name', max_length=100)
    mail = models.EmailField(u'E-mail', max_length=254)

    def __str__(self):
        return self.name
