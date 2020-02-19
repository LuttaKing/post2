from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=700)
    text = models.TextField(max_length=300000)
    # another = models.CharField(max_length=200)
