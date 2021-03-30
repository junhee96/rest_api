from django.urls import path, include
from .views import ProdcutCreateView, ProdcutDetailListView, ProdcutListView, ProdcutUpdateView, ProdcutDeleteView

urlpatterns = [
    path('create/', ProdcutCreateView.as_view()),
    path('detail/<int:pk>/', ProdcutDetailListView.as_view()),
    path('list/', ProdcutListView.as_view()),
    path('update/<int:pk>/', ProdcutUpdateView.as_view()),
    path('delete/<int:pk>/', ProdcutDeleteView.as_view()),
]
