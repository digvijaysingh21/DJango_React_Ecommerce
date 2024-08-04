from rest_framework import generics,permissions

from . import serializers
from . import models

#vendor list
#ListCreateAPIView listing the data and adding the data
class VendorList(generics.ListCreateAPIView):
    queryset= models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer



#Vendor detail
#RetrieveUpdateDestroyAPIView retrieve,update and destroy a single data 
#means responsible for fetching the single data , updating the single data and destroying the single data
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer

#Product List
class ProductList(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer

#Product detail
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer