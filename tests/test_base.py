from rest_framework.test import APITestCase
from accounts.models import Account
from django.urls import reverse
class BaseTest(APITestCase):
    def setUp(self):
        self.admin = Account.objects.create_superuser(
            email='base@gmailcom',
            first_name = 'john',
            last_name ='doe',
            username ='basikk',
            password ='12345'
        )

        self.user = Account.objects.create_user(
            email='sley@gmailcom',
            first_name = 'john',
            last_name ='diss',
            username ='sley463',
            password ='12345'
        )

        self.product_url = reverse('product')
        self.category_url = reverse('category')
        self.cart_url = reverse('cart')
        self.order_url = reverse('order')
        self.info_url = reverse('info')
        self.product_detail_url = lambda id: reverse('product-detail', args=[id])
        self.cart_detail_url = lambda id: reverse('cart-detail', args=[id])
        self.category_detail_url = lambda id: reverse('category-detail', args=[id])
