from django.db import models
from author.models import *
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    publish_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    version=models.IntegerField(default=1)
    image=models.ImageField(upload_to='book/images')
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    @classmethod
    def addbook(cls,title,version,image,authorid):
        author=Author.objects.get(id=authorid)
        Book.objects.create(title=title,version=version,image=image,author=author)
        return True
    