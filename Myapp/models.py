from django.db import models

# Create your models here.
class Data(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    publisher=models.CharField(max_length=100)
    class Meta: 
        verbose_name_plural="Data"