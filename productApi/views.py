from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import routers, serializers, viewsets
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import serializers
from rest_framework_swagger.views import get_swagger_view
from datetime import datetime
import json
from rest_framework.views import APIView

class ProductView(APIView):
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
        
    # @product_list will handle GET and POST calls
    @api_view(['GET', 'POST'])
    def product_list(request):        
        if request.method == 'GET':        
            try: 
                products = Product.objects.all()
                
                title = request.GET.get('name', None)
                if title is not None:
                    products = products.filter(title__icontains=title)
                
                products_serializer = ProductSerializer(products, many=True)
                return JsonResponse(products_serializer.data, safe=False)
            except Exception as e:
                return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'POST':  
            try:
                #import pdb; pdb.set_trace()                
                product_data = JSONParser().parse(request)
                if isinstance(product_data['developers'], list):
                    product_data['developers'] = json.dumps(product_data['developers'])
                else:
                    #product_data['developers'] = json.loads(product_data['developers'])
                    product_data_arry = product_data['developers'].split(',')
                    product_developer = []
                    for p_d in product_data_arry:
                        product_developer.append({'name': p_d})

                    #product_data['developers'] = json.dumps(product_developer)
                    product_data['developers'] = product_developer               

                product_serializer = ProductSerializer(data=product_data)
                if product_serializer.is_valid():
                    product_serializer.save()
                    #import pdb; pdb.set_trace() 
                    #problem is here we needed to return data so i can be parsed.
                    return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except  Exception as e:
                return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)        
    
    # Rest View to handle PUT, PATCH and DELETE calls
    @api_view(['GET', 'PUT', 'PATCH','DELETE'])
    def product_detail(request, pk):
        try: 
            product = Product.objects.get(pk=pk)
            if request.method == 'GET':             
                product_serializer = ProductSerializer(product) 
                return JsonResponse(product_serializer.data) 
            elif request.method == 'DELETE': 
                    product.delete() 
                    return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        
            elif request.method == 'PATCH': 
                    product_data = JSONParser().parse(request)
                    product_data['developers'] = json.loads(product_data['developers'])                
                    product_serializer = ProductSerializer(data=product_data)                
                    if product_serializer.is_valid():
                        instance = product_serializer.update(product, product_data)
                        return JsonResponse(product_data, status=status.HTTP_201_CREATED, safe=False) 
                    return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
        except Exception as e:
            return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)  
    
    @api_view(['GET'])
    def import_data(request):
        #import pdb; pdb.set_trace()
        return JsonResponse({'message': 'Product was deleted successfully!'}) 

    @api_view(['GET'])
    def product_list_published(request):
        pass