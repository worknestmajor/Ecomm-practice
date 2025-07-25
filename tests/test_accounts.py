from .test_base import BaseTest
from accounts.models import Account


class AccountTest(BaseTest):
    def setUp(self):
        return super().setUp()
    
    def test_display_info(self):
        self.client.force_authenticate(user = self.user)
        response = self.client.get(self.info_url)
        self.assertEqual(response.data['message'] , self.user.username)