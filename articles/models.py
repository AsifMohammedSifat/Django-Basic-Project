from django.db import models

# Create your models here.

class article(models.Model):
    title = models.TextField()
    content = models.TextField()