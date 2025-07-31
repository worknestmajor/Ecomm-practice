from .test_base import BaseTest
# from accounts.models import Account


class AccountTest(BaseTest):
    def setUp(self):
        return super().setUp()
    
    def test_create_new_staff(self):
        self.client.force_authenticate(user = self.admin)
        data ={
            'first_name':'john',
            'last_name':'doe',
            'email':'john@gmail.com',
            'username':'johny',
            'password':'12345',
            'role':'staff'
        }
        response =self.client.post(self.staff_url, data)
        self.assertEqual(response.status_code , 200)