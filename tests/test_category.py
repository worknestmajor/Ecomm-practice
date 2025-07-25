from category.models import Category
from rest_framework import status
from .test_base import BaseTest

class CategoryTest(BaseTest):
    def setUp(self):
        return super().setUp()
    
    def test_create_category(self):
        self.client.force_authenticate(user = self.admin)

        data = {
            'category_name':'electronics',
            'category_description':'this is electronic cat'
        }

        response = self.client.post(self.category_url,data)
        self.assertEqual(response.data['message']['category_name'] , 'electronics')
    

    def test_get_category(self):
        category = Category.objects.create(
            category_name = 'elec',
            category_description = 'this is cat'
        )

        response = self.client.get(self.category_detail_url(category.id))

        self.assertEqual(response.data['message']['category_name'], 'elec')
    
    def test_delete_category(self):
        cat = Category.objects.create(
            category_name = 'elec',
            category_description = 'this is cat'
        )
        self.client.force_authenticate(user = self.admin)

        response = self.client.delete(self.category_detail_url(cat.id))
        self.assertEqual(response.status_code , status.HTTP_200_OK)
