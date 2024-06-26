from rest_framework import serializers
from .models import User, Category, Product, SaleOn


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SaleOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOn
        fields = "__all__"
