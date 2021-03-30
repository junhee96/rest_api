from rest_framework import serializers 
from .models import Order
from accounts.serializers import ProfileSerializer
from django.core.validators import ValidationError
from rest_framework.serializers import ReadOnlyField

class OrderCreateSerializer(serializers.ModelSerializer):
    '''
    주문 하기 serializer
    SerializerMethodField를 활용하여 고객의 주소와 상품의 재고의 데이터를 가져옴 
    '''
    address = serializers.SerializerMethodField('get_address')
    def get_address(self, obj):
        return obj.user.address

    stock = serializers.SerializerMethodField('get_stock')
    def get_stock(self, obj):
        return obj.products.stock

    class Meta:
        model = Order
        fields = ("id", "user", "products", "quantity", "address", "stock")
        

class OrderListSerializer(serializers.ModelSerializer):
    '''
    주문 조회하기 serializer
    lookup_field는 기본값이 주문_기본키(id)로 설정 되어 있으므로 고객_정보로 바꿈 
    '''
    class Meta:
        model = Order
        fields = ("id", "user", "products", "quantity")
        lookup_field = 'user'
