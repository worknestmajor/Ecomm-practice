from cart.models import Carts
from .test_base import BaseTest
from rest_framework import status
from product.models import Products
from category.models import Category
# from orders.models import Order,OrderItem

class OrderTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(category_name = "Electronics",category_description ="electronics caegory")
        self.product = Products.objects.create(
            product_name = 'fan',
            stock =10,
            description ='hawells',
            price = 100,
            category = self.category
        )

    def test_create_order(self):

        self.client.force_authenticate(user = self.user)
        cart = Carts.objects.create(
            quantity = 2,
            product = self.product,
            user = self.user
        )
        data ={
            "address":"Pune Warje"
        }

        response = self.client.post(self.order_url, data)

        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
    
    