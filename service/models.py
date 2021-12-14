from django.db import models

# Create your models here.
class Service(models.Model):
    service_id= models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.service_name
