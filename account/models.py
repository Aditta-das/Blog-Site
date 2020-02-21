from django.db import models

class User(models.Model):
    username = models.CharField('Username', max_length=50)
    email = models.CharField('email', max_length=50)
    password = models.CharField('password', max_length=50)

    def __str__(self):
        return self.username