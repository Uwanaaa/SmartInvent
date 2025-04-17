from .base_repository import BaseRepo
from users.models import User

class UserRepo(BaseRepo):
    """
    Initializing the User repository to ensure separation of concerns in database access, promoting better organization and maintainability.
    """
    def __init__(self, model):
        super().__init__(User)
