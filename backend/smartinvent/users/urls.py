from django.urls import path
from .views import CreateUser,ObtainToken,LogoutUser,GetUser,UpdateUser
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('create/', CreateUser.as_view(), name='create_user'),
    path('login/', ObtainToken.as_view(), name='token_obtain_pair'),
    path('logout/',LogoutUser.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-user/',GetUser.as_view()),
    path('update-user/',UpdateUser.as_view())
]

