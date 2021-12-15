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


class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    service_type=models.CharField(max_length=200)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.TextField()
    area = (
        ('Civil', 'Civil Lines'),
        ('Shanti', 'Shatipuram')
        
    )
    city = models.CharField(max_length=10, choices=area)

    

    # name = models.CharField(max_length=100, blank=True, default='')

