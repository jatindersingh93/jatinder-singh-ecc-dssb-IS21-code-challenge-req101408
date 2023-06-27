#from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers 
from .models import Product

# Serialize data
class ProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.ownerName = validated_data.get('ownerName', instance.ownerName)
        instance.masterName = validated_data.get('masterName', instance.masterName)
        instance.startDate = validated_data.get('startDate', instance.startDate)
        instance.developers = validated_data.get('developers', instance.developers)
        instance.methodology = validated_data.get('methodology', instance.methodology)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance