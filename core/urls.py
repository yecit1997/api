
from django.urls import path, include
from rest_framework import routers
from .views import UserView, CategoryView, PoductView, SaleOnView

router = routers.DefaultRouter()
router.register(r'user', UserView, 'user')
router.register(r'category', CategoryView, 'category')
router.register(r'product', PoductView, 'product')
router.register(r'sale', SaleOnView, 'sale')

urlpatterns = [
    path('', include(router.urls)),
]
