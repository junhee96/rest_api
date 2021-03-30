from rest_framework import permissions, generics, status
from rest_framework.response import Response
from .serializers import OrderCreateSerializer,OrderListSerializer
from .models import Order
from accounts.models import User
from product.models import Product
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from knox.models import AuthToken

class OrderCreateView(generics.CreateAPIView):
    '''
    가입된 고객만 주문 하기
    상품의 재고가 0이 되면 주문이 안됨
    유저의 정보에 주소가 없으면 주문이 안됨 
    '''
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.data["user"]
        user_address = User.objects.get(id=user).address
        prod = Product.objects.get(pk=request.data["products"])
        if user_address:
            if prod.stock > 0:
                prod.stock -= int(request.data['quantity'])
                prod.save()
                return self.create(request, *args, **kwargs)
            else:
                return Response({"message": "재고 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "주소가 없습니다"}, status=status.HTTP_400_BAD_REQUEST)

class OrderListView(generics.ListAPIView):
    '''
    해당 유저 주문 조회
    '''
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):   
        pk = self.kwargs.get("user")
        return Order.objects.filter(user=pk)
        
