from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)

    @classmethod
    def Get_all(cls):
        return [(auth.id,auth.name) for auth in cls.objects.all()]