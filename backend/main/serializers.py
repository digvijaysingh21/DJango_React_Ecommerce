from rest_framework import serializers
from . import models

#Vendor List serializer
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']


    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


#Vendor Detail serializer
class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth=1



#Product List serializer
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','detail','price']

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth=1


#Product detail Serializer
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id','category','vendor','title','detail','price']

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth=1