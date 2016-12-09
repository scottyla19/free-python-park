from django.db import models
from django.utils.crypto import get_random_string
from django.db import IntegrityError


# Create your models here.
class ShortUrl(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField()
    short_url = models.URLField()
    unique_id = models.CharField(max_length=6, blank=False, editable=False, unique=True)
    base_url =  models.URLField(default = "/shorturl/")

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(length = 6)
        success = False
        failures = 0
        while not success:
            try:
                super(ShortUrl, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:
                    raise
                else:
                    # looks like a collision, try another random value
                    self.unique_id = get_random_string(length = 6)
            else:
                success = True
        if not self.short_url:

            self.short_url = str(self.base_url) + self.unique_id
            super(ShortUrl, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)