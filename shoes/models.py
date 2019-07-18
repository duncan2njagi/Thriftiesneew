from django.db import models


class Shoe(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    color = models.CharField(max_length=100)
    shoe_size = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class About(models.Model):
    who = models.CharField(max_length=350)
    what = models.CharField(max_length=350)
    where = models.CharField(max_length=350)
    why = models.CharField(max_length=350)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.IntegerField()
    address = models.CharField(max_length=50)


class Service(models.Model):
    automation = models.CharField(max_length=255)
    responses = models.CharField(max_length=255)