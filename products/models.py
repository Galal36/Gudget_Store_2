from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True, default='products/img.png')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField(default=0)
    manufacture = models.CharField(max_length=50, default='')
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    def __str__(self):
        return self.name
    
    # def soft_delete(self):
    #     """Performs a soft delete operation"""
    #     self.is_deleted = True
    #     self.save()
