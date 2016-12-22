from django.db import models


# Create your models here.
class ImageSearch(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    term = models.CharField(max_length = 100)

    class Meta:
        ordering = ('created',)