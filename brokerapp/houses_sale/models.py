from django.db import models

# Create your models here.

class HouseList(models.Model):
    location_city = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    reserved = models.BooleanField(default=False, null=True)
    sold = models.BooleanField(default=False, null=True)

    def is_reserved(self):
        """
        returns true if HouseList instance is reserved
        """
        if self.reserved is True:
            return True
        else:
            return False
    
    def is_sold(self):
        """
        returns true if HouseList instance is sold
        """
        if self.sold is True:
            return True
        else:
            return False



    def __str__(self):
        return str(self.pk)