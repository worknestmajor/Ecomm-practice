from cart.models import Carts
from .test_base import BaseTest
from rest_framework import status
from product.models import Products
from category.models import Category

class CartTest(BaseTest):
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
    
    def test_create_cart(self):
        self.client.force_authenticate(user = self.user)
        data ={
            'quantity' : 20,
            'product' : self.product.id,
            'user' : self.user.id
        }
        response = self.client.post(self.cart_url, data)
        
    
    def test_delete_cart(self):
        self.client.force_authenticate(user = self.user)
        cart = Carts.objects.create(
            quantity = 2,
            product = self.product,
            user = self.user
        )
        response = self.client.delete(self.cart_detail_url(cart.id))
        self.assertEqual(response.status_code , status.HTTP_200_OK)

        self.assertEqual(response.status_code , status.HTTP_200_OK)
