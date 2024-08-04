from rest_framework import generics,permissions

from . import serializers
from . import models

#vendor list
class VendorList(generics.ListAPIView):
    queryset= models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permisssion_classes=[permissions.IsAuthenticated]



#Vendor detail
class VendorDetail(generics.RetrieveAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class= serializers.VendorSerializer
    # permisssion_classes=[permissions.IsAuthenticated]

