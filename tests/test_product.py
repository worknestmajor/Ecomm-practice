from product.models import Products
from category.models import Category
from tests.test_base import BaseTest
from rest_framework import status

class ProductModelTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(category_name = "Electronics",category_description ="electronics caegory")

    
    def test_admin_create_product(self):
        self.client.force_authenticate(user=self.admin)
        data = {
            "category": self.category.id,
            "product_name": "Laptop",
            "description": "Gaming laptop",
            "stock": 10,
            "price" :100
        }
        response = self.client.post(self.product_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_single_product(self):
        product = Products.objects.create(
            category=self.category,
            product_name="Headphones",
            description="Bluetooth headphones",
            stock=20,
            price = 100
        )
        url = self.product_detail_url(product.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message']['product_name'], "Headphones")

    
    def test_delete_product(self):
        product = Products.objects.create(
            category=self.category,
            product_name="Speaker",
            description="Wireless Speaker",
            stock=8,
            price = 100
        )
        self.client.force_authenticate(user=self.admin)
        url = self.product_detail_url(product.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Products.objects.count(), 0)