from django.urls import path
from .views import GetAllProducts,CreateProduct,DeleteProduct,UpdateProduct,GetProduct,ProductReplenishmentView,UpdateProvider,GetProvider,TotalProducts,SetAlertValue


urlpatterns = [
    path('', GetAllProducts.as_view()),
    path('create-product/',CreateProduct.as_view()),
    path('get-product/<int:id>/',GetProduct.as_view()),
    path('update-product/<int:id>/',UpdateProduct.as_view()),
    path('delete-product/<int:id>/',DeleteProduct.as_view()),
    path('provider-form/',ProductReplenishmentView.as_view()),
    path('provider/<int:id>/',GetProvider.as_view()),
    path('update-provider/<int:id>/',UpdateProvider.as_view()),
    path('total/',TotalProducts.as_view()),
    path('set-alert-value/',SetAlertValue.as_view())
]
