from django.db import models

""" Neswsletter subscription """

class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    token = models.CharField(max_length=36, null=True)

    def __str__(self):
        return self.email
