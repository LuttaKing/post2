from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=3000)
    # another = models.CharField(max_length=200)