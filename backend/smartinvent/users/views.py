from django.db.utils import IntegrityError
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView,Response
from rest_framework import status
from .repositories.users_repository import UserRepo
from .models import User
from .serializers import UserSerializer,CustomSerializer
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,get_object_or_404





def serve_react(request):
    return render(request, 'index.html')


class ObtainToken(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomSerializer

    def post(self,request,*args, **kwargs):
        response = super().post(request,*args, **kwargs)
        data = response.data
        

        response.set_cookie(
            key = 'access_token',
            value = data['access'],
            httponly = True,
            secure = False,
            samesite = 'Lax',
            max_age = 3600 
        )

        response.set_cookie(
            key = 'refresh_token',
            value = data['refresh'],
            httponly = True,
            secure = False,
            samesite = 'Lax',
            max_age = 86400
        )


        return response

class CreateUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request,*args, **kwargs):
        if request.data:
            print(request.data)
            try:
                created_user = User.objects.create(**request.data)
                if created_user:
                    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                    return Response({"message": "There is already a user with these credentials"}, status=status.HTTP_200_OK)
        return Response({"message": "No data was sent"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args, **kwargs):
        try:
            user_id = kwargs.get('id')
            user_serializer = UserSerializer(data=request.data)

            if user_serializer.is_valid():
                user_serializer.update(id=request.user.id)
                return Response({'message':'Profile has been updated successfully'},status=status.HTTP_200_OK)
            errors = []
            for key,value in user_serializer.errors.items():
                errors.append(value)
            print(user_serializer.errors)
            return Response({'message':errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f'Error: {e}')
            return Response({"message": "Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User,id=request.user.id)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data,status=status.HTTP_200_OK)


class LogoutUser(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,*args, **kwargs):
        response = Response({"message": "Logged out successfully"})
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response