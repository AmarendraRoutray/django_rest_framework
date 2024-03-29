from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import *
from .serializers import SchoolSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def school_json_data(request):
    SO=School.objects.all()
    JO=SchoolSerializer(SO,many=True)
    json_data=JO.data
    return Response(json_data)

@api_view(['POST'])
def post_data(request):
    SO = SchoolSerializer(data=request.data)
    if SO.is_valid():
        SO.save()
        return Response({'Success':'Data inserted'})
    else:
        return Response({'Error':'Failed'})