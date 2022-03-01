from statistics import mode
from unicodedata import name
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return name