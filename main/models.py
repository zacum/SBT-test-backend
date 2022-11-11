from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(
        upload_to="media/", height_field=None, width_field=None, max_length=100
    )
    seckey = models.CharField(max_length=255)


class Degree(models.Model):
    name = models.CharField(max_length=255)


class Mdata(models.Model):
    tokenid = models.IntegerField()
    metadata = models.JSONField()
