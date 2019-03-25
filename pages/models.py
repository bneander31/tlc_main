from django.db import models
from datetime import datetime

class Location(models.Model):
    photo_main = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400)
    photo_1 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_2 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_3 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_4 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_5 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_6 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_7 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_8 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_9 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_10 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_11 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    photo_12 = models.ImageField(upload_to='photos/locations/%Y/%m/', max_length=400, blank=True)
    location_name = models.CharField(max_length=200)
    location_content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    location_url = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.location_name
