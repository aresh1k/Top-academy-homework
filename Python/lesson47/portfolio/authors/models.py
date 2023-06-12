from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
