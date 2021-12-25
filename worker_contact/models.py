from django.db import models
from django.core.exceptions import ValidationError

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
    
    def clean(self):
        if self.phone < 1000000000 or self.phone > 9999999999:
            raise ValidationError("Length of phone 1 is wrong")

        if self.adhar_card < 100000000000 or self.adhar_card > 999999999999:
            raise ValidationError("Length of Adhar Card is wrong")