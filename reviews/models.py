from django.db import models

from profiles.models import UserProfile
from products.models import Product

from django.contrib.auth.models import User


class Review(models.Model):
    """ 
    Creates a reviews model
    """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    comment = models.TextField(max_length=1000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
