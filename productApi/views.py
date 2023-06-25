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
from rest_framework_swagger.views import get_swagger_view

@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):   
    
    if request.method == 'GET':
        #import pdb; pdb.set_trace()
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
            product_data = JSONParser().parse(request)
            product_data['startDate'] = '2020-03-11'
            del  product_data['isEdit'] 
            #del  product_data['isEdit'] 
            del product_data['isSelected']
            del product_data['id']
            import pdb; pdb.set_trace()

            product_serializer = ProductSerializer(data=product_data)
            #import pdb; pdb.set_trace()
            if product_serializer.is_valid():
                product_serializer.save()
                return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except  Exception as e:
             return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)        
 
@api_view(['GET', 'PUT', 'PATCH'])
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
                product_serializer = ProductSerializer(data=product_data)                
                if product_serializer.is_valid():
                    product_serializer.save()
                    return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
    except Exception as e:
        return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)  
       
        
@api_view(['GET'])
def product_list_published(request):
    pass