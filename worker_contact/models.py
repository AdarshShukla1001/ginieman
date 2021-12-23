from django.db import models

# Create your models here.

class WorkingMan(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    phone2=models.BigIntegerField()
    adhar_card=models.BigIntegerField(default=0)
    email=models.EmailField( max_length=250,null=True)
    service_names=models.CharField(max_length=200)
    address=models.TextField()
    image_url=models.URLField()