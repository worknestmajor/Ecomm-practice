from rest_framework import serializers
from .models import Order, OrderItem
from cart.models import Carts

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source='items', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'address', 'order_items']
        read_only_fields = ['user', 'status', 'total_price']

    def create(self, validated_data):
        request = self.context['request']
        user = request.user

        cart_items = Carts.objects.filter(user=user)

        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty.")

        order = Order.objects.create(user=user, address=validated_data['address'])

        total_price = 0
        for cart_item in cart_items:
            product = cart_item.product
            quantity = cart_item.quantity
            price = product.price 

            if product.stock < quantity:
                raise serializers.ValidationError("limited sock")

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )

            total_price += price * quantity
            product.stock -= quantity
            product.save()

            


        order.total_price = total_price
        order.save()

        # Clear the user's cart
        cart_items.delete()

        return order