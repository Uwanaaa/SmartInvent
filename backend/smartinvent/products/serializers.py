from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Product,ProductReplenishment

class ProductSerializer(serializers.ModelSerializer):
    provider_id = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'  

    def get_provider_id(self,obj):
        provider = obj.provider.first()
        if provider:
            return provider.id
        return None


class ProductReplenishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReplenishment
        fields = '__all__'  
        
    def update(self,id,data,*args, **kwargs):
     try: 
        provider = get_object_or_404(ProductReplenishment,id=id)
    
        for key,value in data.items():
            setattr(provider,key,value)
        provider.save()
        return provider
     except Exception as e:
        print(f'Error: {e}')
        return None