from django.db import models


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
