from django.urls import path, include
from .views import SignUpAPIView, LoginAPIView, ProfileUpdateAPI
'''
knox를 활용하여 토큰 생성을 하엿기 때문에
auth/logout/ 로 접속하면 가입된 고객 logout이 된다
'''
urlpatterns = [
    path('auth/signup/', SignUpAPIView.as_view()),
    path('auth/login/', LoginAPIView.as_view()),
    path("auth/profile/<int:pk>/", ProfileUpdateAPI.as_view()),
]
