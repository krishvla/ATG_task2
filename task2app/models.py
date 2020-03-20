from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

class articles(models.Model):
    article_name = models.CharField(max_length=30,default='default name')
    content = models.CharField(max_length=500)
    username = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    publish = models.CharField(max_length=8,default='private')