from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from drf_yasg import openapi

schema_url_patterns = [
    path('accounts/', include('accounts.urls')),
    path('order/', include("order.urls")),
    path('product/', include("product.urls")),
]
 
schema_view = get_schema_view(
    openapi.Info(
        title="Open API",
        default_version='v1',
        description = 
        '''
        Open API 문서 페이지 입니다.
        ''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tyyt0528@likelion.org"),
        license=openapi.License(name="이준희"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)