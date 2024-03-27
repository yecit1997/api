from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Category, Product, SaleOn
from .serializer import (
    UserSerializer,
    CategorySerializer,
    ProductSerializer,
    SaleOnSerializer,
)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PoductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SaleOnView(viewsets.ModelViewSet):
    serializer_class = SaleOnSerializer
    queryset = SaleOn.objects.all()
