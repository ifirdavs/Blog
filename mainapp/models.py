from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    job = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    head = models.CharField(max_length=60)
    date = models.DateField(auto_now_add=True)
    topic = models.CharField(max_length=60)
    text = models.CharField(max_length=600)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return f"{self.head}, {self.author.name}"