from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    google_map_link = models.URLField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.place_name
