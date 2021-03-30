from rest_framework import permissions, generics, status
from rest_framework.response import Response
from .serializers import SignUpSerializer, LoginSerializer, ProfileSerializer
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from knox.models import AuthToken

class SignUpAPIView(generics.GenericAPIView):
    '''
    회원가입 비밀번호 5자 이상이여야 생성가능
    knox 활용 하여 토큰을 생성하여 암호화 형태로 저장 만료 시간 기본값인 10시간
    '''
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if len(request.data["password"]) < 4:
            body = {"message": "비빌번호 5자 이상"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": SignUpSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )
        
class LoginAPIView(generics.GenericAPIView):
    '''
    로그인 기능
    '''
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": LoginSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class ProfileUpdateAPI(generics.RetrieveUpdateAPIView):
    '''
    고객 기본키 값을 url 주소로 접속하여 해당하는 기본키값 회원 정보만 조회 가능
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(User, pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

