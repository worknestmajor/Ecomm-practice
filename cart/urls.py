from django.urls import path
from .views import CartView

urlpatterns = [
    path('cart/', CartView.as_view(), name= "cart"),
    path('cart/<int:pk>/', CartView.as_view(), name="cart-detail")
]