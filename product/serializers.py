from rest_framework import serializers 
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    '''
    주문 조회하기 serializer
    lookup_field는 기본값이 주문_기본키(id)로 설정 되어 있으므로 고객_정보로 바꿈 
    '''
    class Meta:
        model = Product
        fields = ("id", "name", "manufacturer", "stock", "price", "shelf_life")

