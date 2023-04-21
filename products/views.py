from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import *
from .models import *


@api_view(['POST'])
@csrf_exempt
def post_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        images = request.FILES.getlist('pictures')
        product = serializer.save()
        for image in images:
            Image.objects.create(product=product, image=image)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        print('entry not valid')
        return Response(serializer.errors, status=400)
    


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)



@api_view(['POST', 'GET'])
@csrf_exempt
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        images = request.FILES.getlist('images')
        product = serializer.save()
        for image in images:
            Image.objects.create(product=product, image=image)
    else:
        return Response(serializer.errors, status=400)
    return Response(serializer.data) 



@api_view(['POST'])
@csrf_exempt
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('deleted')
