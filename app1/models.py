from django.db import models
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='items')
    stock_status = models.CharField(max_length=100)
    available_stock = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
