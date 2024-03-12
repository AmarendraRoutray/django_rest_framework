from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from .models import Product
from .serializers import ProductModelSerializer
from rest_framework.response import Response


class ProductCrup(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
        JO=ProductModelSerializer(LPO,many=True)
        return Response(JO.data)
    
    def retrieve(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JO=ProductModelSerializer(PO)
        return Response(JO.data)
    
    def create(self,request):
        JD=request.data
        PO=ProductModelSerializer(data=JD)
        if PO.is_valid():
            PO.save()
            return Response({'Success':'Data inserted'})
        else:
            return Response({'Error':'Failed'})
    
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductModelSerializer(PO,data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Success':'Updated'})
        else:
            return Response({'Error':'Failed to update'})
        
    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        PDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Success':'Data Updated'})
        else:
            return Response({'Error':'Failed to update'})
        
    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Deletion':'Data deleted'})
        