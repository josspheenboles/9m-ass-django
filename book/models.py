from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    publish_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    version=models.IntegerField(default=1)
    image=models.CharField(max_length=100)

    