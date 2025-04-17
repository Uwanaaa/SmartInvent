from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView,Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import Product,ProductReplenishment
from users.models import User
from .permissions import isAdmin
from .serializers import ProductReplenishmentSerializer,ProductSerializer



class CreateProduct(APIView):
   permission_classes = [isAdmin,IsAuthenticated]

   def post(self,request,*args, **kwargs):
     try:
      serializer = ProductSerializer(data=request.data)
      request.session['product'] = request.data.get('name')

      if serializer.is_valid():
         serializer.save()
         return Response({'message':'Product has been added successfully'},status=status.HTTP_201_CREATED)
      return Response({'message':'A product with this name exists already'},status=status.HTTP_200_OK)
     except Exception as e:
           print(f'Error: {e}')
           return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   

class GetAllProducts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args, **kwargs):
       try: 
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response({'product':serializer.data},status=status.HTTP_200_OK)
       except Exception as e:
           print(f'Error: {e}')
           return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class GetProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
       try: 
        product_id = kwargs.get('id') 
        product = get_object_or_404(Product, id=product_id)  
        product.refresh_from_db() 
        serializer = ProductSerializer(product) 
        request.session['product'] = product.name
    
        return Response(serializer.data, status=status.HTTP_200_OK)
       except Exception as e:
          print(f'Error: {e}')
          return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateProduct(APIView):
    permission_classes = [isAdmin, IsAuthenticated]

    def post(self, request, *args, **kwargs):
       try: 
        product_id = kwargs.get('id')
        product = get_object_or_404(Product,id=product_id)
        for key, value in request.data.items(): 
            setattr(product, key, value)
        product.save() 
        return Response({'message': 'The product has been updated successfully'}, status=status.HTTP_200_OK)
       except Exception as e:
           print(f'Error: {e}')
           return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteProduct(APIView):
    permission_classes = [isAdmin, IsAuthenticated]

    def delete(self,request,*args, **kwargs):
       try: 
        id = kwargs.get('id')
        if id:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({'message': 'The product has been deleted successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'No id was provided'}, status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
           print(f'Error: {e}')
           return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       

class ProductReplenishmentView(APIView):
    permission_classes = [isAdmin,IsAuthenticated]

    def post(self,request,*args, **kwargs):
     try:
        replenish_serializer = ProductReplenishmentSerializer(data=request.data)
        print(f'Product: {self.request.session.get('product',None)}')
        product = Product.objects.get(name=self.request.session.pop('product',None))
        

        if replenish_serializer.is_valid():
            replenish_serializer.save(product=product,active=True)
            return Response({"message":"The provider information has been saved successfully"},status=status.HTTP_201_CREATED)
        errors = []
        for error_field,value in replenish_serializer.errors.items():
         errors.append(value)
        return Response({"message": errors}, status=status.HTTP_400_BAD_REQUEST)
     except Exception as e:
        print(f'Error: {e}')
        return Response({"message": "Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateProvider(APIView):
   permission_classes = [IsAuthenticated]

   def post(self,request,*args, **kwargs):
     try: 
        id = kwargs.get('id')
        if id:
         replenish_serializer = ProductReplenishmentSerializer(data=request.data)

        if replenish_serializer.is_valid():
            replenish_serializer.update(id=id,data=replenish_serializer.validated_data)
            return Response({'message':'The provider information has been updated successfully'},status=status.HTTP_200_OK)
        
        errors = []
        for error_field,value in replenish_serializer.errors.items():
            errors.append(value)
        return Response({'message': errors}, status=status.HTTP_400_BAD_REQUEST)
     except Exception as e:
        print(f'Error: {e}')
        return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetProvider(APIView):
   permission_classes = [IsAuthenticated,isAdmin]

   def get(self,request,*args, **kwargs):
     try:
      provider_id = kwargs.get('id')
      provider = get_object_or_404(ProductReplenishment,id=provider_id)
      serializer = ProductReplenishmentSerializer(provider)
      return Response(serializer.data,status=status.HTTP_200_OK)
     except Exception as e:
        print(f'Error: {e}')
        return Response({'message':'Server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   

class SetAlertValue(APIView):
   permission_classes = [IsAuthenticated]

   def post(self,request,*args, **kwargs):
     try: 
      user = get_object_or_404(User,username=request.user)
      user.alert_value = request.data.get('alert_value')
      user.save()
      return Response({'message':'The alert value has been set successfully'},status=status.HTTP_201_CREATED)
     except Exception as e:
        print(f'Error: {e}')
        return Response({'message':'Server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
      
          
class TotalProducts(APIView):
   permission_classes = [IsAuthenticated]

   def get(self,request,*args, **kwargs):
     try:
      count = Product.objects.count()
      return Response({'count':count},status=status.HTTP_200_OK)
     except Exception as e:
        print(f'Error: {e}')
        return Response({'message':'Server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)