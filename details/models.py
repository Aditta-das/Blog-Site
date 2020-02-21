from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username