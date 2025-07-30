from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Carts
from .serializers import CartSerializer
# from product.models import Products

from drf_spectacular.utils import extend_schema
class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Carts.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    

    @extend_schema(
            request=CartSerializer,
            responses=CartSerializer,
            description="Create Cart"
    )
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data['product']
            quantity = serializer.validated_data.get('quantity', 1)
            cart_item = Carts.objects.filter(user = request.user, product = product).first()
            if cart_item:
                cart_item.quantity += quantity
                cart_item.save()
            else:
                cart_item = Carts.objects.create(
                    product = product,
                    quantity = quantity,
                    user = request.user
                )
            return Response(CartSerializer(cart_item).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({"error": "ID required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = Carts.objects.get(pk=pk, user=request.user)
            cart_item.delete()
            return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
        except Carts.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
