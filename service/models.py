
from django.db import models


# Model For Service
class Service(models.Model):
    service_id= models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.service_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

    service_name=models.CharField(max_length=200)
    email=models.CharField(max_length=300,null=True)
    
    number=models.IntegerField()
    locality=models.CharField(max_length=100)
    address=models.TextField()
    date=models.DateField(null=True, blank=True,default='')
    time=models.TimeField(null=True, blank=True,default='')
    date_ordered = models.DateTimeField(auto_now=True)

    


    









# # City Model
# class City(models.Model):
#   name = models.CharField(max_length=100)
  
#   def __str__(self):
#         return str(self.name)
    
# # Locality
# class Locality(models.Model):
#   country = models.ForeignKey(
#           City, 
#           on_delete=models.CASCADE
#   )
#   name = models.CharField(max_length=100)
  
#   def __str__(self):
#         return str(self.name)