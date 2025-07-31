from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer

from drf_spectacular.utils import extend_schema, OpenApiExample,OpenApiParameter

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
            description="**This is used to get all orders**",
            
            responses={200: OrderSerializer(many=True)},
    )
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @extend_schema(
            description="create new Order",
            request=OrderSerializer,
            responses=OrderSerializer,
            examples=[
                OpenApiExample(
                    
                    name='order'
                    ,description='Create order'
                    ,value={
                
                        "address": "string",
                        
                    },
                    request_only= True
                    
                ),
                OpenApiExample(
                    
                    name='order'
                    ,description='Create order'
                    ,value={
                        "id": 1,
                        "user": 1,
                        "total_price": 100,
                        "address": "string",
                        "order_items": [
                            {
                            "id": 1,
                            "product": 1,
                            "product_name": "demo product name",
                            "quantity": 10,
                            "price": 10
                        }
                    ]
                    },
                    response_only = True
                    
                )
                

            ],
            # parameters=[
            #     OpenApiParameter(
            #         address='pune'
            #     )
            # ]
    )
    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

