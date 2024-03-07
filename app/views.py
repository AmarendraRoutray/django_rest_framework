from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from .models import *
from .serializers import ProductModelSerializer
from rest_framework.response import Response


class ProductCrud(APIView):
    def get(self,request,id):
        PO=Product.objects.all()
        JO=ProductModelSerializer(PO,many=True)
        # PO=Product.objects.get(product_id=id)
        # JO=ProductModelSerializer(PO)
        data=JO.data
        return Response(data)
    
    def post(self,request,id):
        # JO=request.data # request.data is dict
        PO=ProductModelSerializer(data=request.data)
        if PO.is_valid():
            PO.save()
            return Response({'Message':'Data inserted Successfully!!'})
        else:
            return Response({'Error':'Data not inserted'})
        
    def put(self,request,id):
        UPO=Product.objects.get(product_id=id)
        PO=ProductModelSerializer(UPO,data=request.data)
        if PO.is_valid():
            PO.save()
            return Response({'Success':'Data updated'})
        else:
            return Response({'Error':'Unable to update data'})
        
    def patch(self,request,id):
        UPO=Product.objects.get(product_id=id)
        PO=ProductModelSerializer(UPO,data=request.data,partial=True)
        if PO.is_valid():
            PO.save()
            return Response({'Success':'Data updated'})
        else:
            return Response({'Error':'Unable to update data'})
        
    def delete(self,request,id):
        Product.objects.get(product_id=id).delete()
        return Response({'Deletion':'Data deleted'})