from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  owner = models.CharField(max_length=100)
  cover = models.ImageField(upload_to='covers/')

