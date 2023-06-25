#from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers 
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # isEdit = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    
    # def isEdit(self, obj):
    #     return False