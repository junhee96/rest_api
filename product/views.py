from rest_framework import generics
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAdminUser


class ProdcutCreateView(generics.CreateAPIView):
    '''
    관리자만 상품 생성
    '''
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProdcutDetailListView(generics.ListAPIView):
    '''
    관리자만 해당하는 상품 조회
    '''
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):   
        pk = self.kwargs.get("pk")
        return Product.objects.filter(pk=pk)

class ProdcutListView(generics.ListAPIView):
    '''
    관리자만 상품 전체 조회
    '''
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()

class ProdcutUpdateView(generics.RetrieveUpdateAPIView):
    '''
    관리자만 해당하는 상품 수정
    '''
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()

class ProdcutDeleteView(generics.RetrieveDestroyAPIView):
    '''
    관리자만 해당하는 상품 삭제
    '''
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()


