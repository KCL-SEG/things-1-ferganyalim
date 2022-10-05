from django.db import models

class Thing(Model):
    name = models.TextField()
    description = models.TextField()
    quantity = models.PositiveIntegerField()
