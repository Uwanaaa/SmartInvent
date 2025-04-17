from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser
import threading


_user = threading.local()

class CustomJWTMiddleware(MiddlewareMixin):
    def process_request(self,request):
        jwt = JWTAuthentication()
        token = request.COOKIES.get('access_token')

        if token:
            try:
                validated_token = jwt.get_validated_token(token)
                request.user = jwt.get_user(validated_token)
                _user.value = request.user
            except:
                request.user = AnonymousUser
                
def get_current_user():
     return getattr(_user, 'value', None)



