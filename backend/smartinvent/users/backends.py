from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if username is None and password is None:
            username = request.user.username
            try:
                user = User.objects.get(username=username)
                if user.check_password(request.user.password):
                 return user
            except User.DoesNotExist:
                    return None
            
    def get_user(self, user_id):
        return super().get_user(user_id)
