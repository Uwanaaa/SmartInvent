from users.repositories.base_repository import BaseRepo
from ..models import Product

class ProductRepo(BaseRepo):
    """
    Initializing the Product repository to ensure separation of concerns in database access, promoting better organization and maintainability.
    """
    def __init__(self, model):
        super().__init__(Product)
