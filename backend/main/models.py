from django.db import models
from django.contrib.auth.models import User

'''

In Django, the on_delete parameter is used in foreign key and one-to-one relationships to specify the behavior that should be applied when the referenced object is deleted. Here’s a quick explanation of the two options you mentioned:

on_delete=models.CASCADE: This will delete the object that references the deleted object. For example, if you have a foreign key in a model and the referenced object is deleted, then the object containing the foreign key will also be deleted.

on_delete=models.SET_NULL: This will set the foreign key to NULL when the referenced object is deleted. This requires that the foreign key field is nullable (i.e., null=True).


Example for understanding:

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # CASCADE option

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)  # SET_NULL option

In this example:

If an Author is deleted, all Book instances related to that Author will also be deleted because of on_delete=models.CASCADE.
If a Publisher is deleted, the publisher field in related Book instances will be set to NULL because of on_delete=models.SET_NULL.


'''



# Vendor Models

class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)

    def __str__(self):
        return self.user.username

#Product category
class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)

    def __str__(self):
        return self.title

#Product
class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL, null=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    price=models.FloatField()



    def __str__(self):
        return self.title
