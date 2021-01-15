from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_name=models.CharField(max_length=15)

    def __str__(self):
        return self.user_name

class Category(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.title

class Product (models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to='products')
    first_link=models.URLField(blank=False)
    second_link=models.URLField(blank=True)

    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    first_price=models.FloatField()
    second_price=models.FloatField(null=True, blank=True)

    description=models.TextField()

    def __str__(self):
        return self.title


