from django.db import models


class Art(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='arts/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
