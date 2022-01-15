from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('apis:create')
CREATE_TOKEN_URL = reverse('apis:token_obtain_pair')

# TOKEN_URL = reverse('user:token')
# ME_URL = reverse('user:me')
def create_user(params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(params)

class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_valid_payload_success(self):
        """Test creating using with a valid payload is successful"""
        payload = {
            'phone': '+919656248731',
            'password': 'testpass',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
    
    def test_create_user_with_invalid_phone_fail(self):
        """Test creating using with a valid payload is successful"""
        payload = {
            'phone': '+91965dfgdf62487',
            'password': 'testpass',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_token_create(self):


        payload = {
            'phone': '+919656248731',
            'password': 'testpass',
        }
        self.client.post(CREATE_USER_URL, payload)
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_unauthorized(self):
    

        payload = {
            'phone': '+919656248731',
            'password': 'testpass',
        }
        self.client.post(CREATE_USER_URL, payload)
        payload = {
            'phone': '+919656248731',
            'password': 'testpass',
        }
        res = self.client.post(CREATE_TOKEN_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)