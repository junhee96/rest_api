from django.urls import path, include
from .views import OrderCreateView, OrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path("orderlist/<int:user>/", OrderListView.as_view()),

]
