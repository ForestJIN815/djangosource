from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.name
