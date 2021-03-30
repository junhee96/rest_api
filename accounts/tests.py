from django.test import Client
import json
from .models import User
from rest_framework.test import APITestCase


client = Client()

class Account_test(APITestCase):     
    def test_signup(self):
        user = {
            'username' : "qwer4242@naver.com",
            'password' : 'qwer123',
            'nickname' : "홍길동",
            'phone' : "0105689532",
            'address' : "서울특별시",
            'gender' : ""
        }
        response = client.post('/accounts/auth/signup/',user, format='json' )
        self.assertEqual(response.status_code, 200)

        user_login = {'username': 'qwer4242@naver.com', 'password': 'qwer123'}
        response_login = client.post('/accounts/auth/login/',user_login, format='json')
        self.assertEqual(response_login.status_code, 200)
    
