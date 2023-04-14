import time

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.cache import cache
from rest_framework.test import APITestCase

from users.utils import get_tokens_for_user

user_model = get_user_model()


class SignupFlowTestCase(APITestCase):
    SIGNUP_ENDPOINT = 'signup'
    VERIFY_PHONE_ENDPOINT = 'verify_phone'
    VERIFY_EMAIL_ENDPOINT = 'verify_email'
    SIGNIN_ENDPOINT = 'signin'

    def test_signup_user(self):
        # Testing signup user API
        self.data = {
            'email': 'testcase@test.com',
            'phone': '09107412876',
            'password': '12345678',
        }
        response = self.client.post(reverse(self.SIGNUP_ENDPOINT), self.data)
        self.assertEqual(response.status_code, 201)

        # Testing verify user phone API
        time.sleep(0.009)
        code = cache.get(self.data.get('phone'))
        self.req_data = {
            'phone': self.data.get('phone'),
            'code': code
        }
        response = self.client.post(
            reverse(self.VERIFY_PHONE_ENDPOINT), self.req_data)
        self.assertEqual(response.data, {'phone_verified': True})

        # Testing verify user email API
        code = cache.get(self.data.get('email'))
        self.req_data = {
            'email': self.data.get('email'),
            'code': code
        }
        response = self.client.post(
            reverse(self.VERIFY_EMAIL_ENDPOINT), self.req_data)
        self.assertEqual(response.data, {'email_verified': True})

        # Testing signin user phone API
        self.req_data = {
            'phone_or_email': '09107412876',
            'password': '12345678'
        }
        response = self.client.post(
            reverse(self.SIGNIN_ENDPOINT), self.req_data)
        self.assertEqual(response.status_code, 201)


class UserDetailFlowTestcase(APITestCase):
    SIGNIN_ENDPOINT = 'signin'
    USER_DETAIL_ENDPOINT = 'user_detail'
    USER_CHANGE_PASSWORD_ENDPOINT = 'user_change_password'

    def test_signin_user(self):
        # Setting up a user
        self.data = {
            'email': 'testcase@test.com',
            'phone': '09107412876',
            'password': '12345678',
            'email_verified': True,
            'phone_verified': True
        }
        self.user = user_model.objects.create_user(**self.data)

        # Testing signin user phone API
        self.req_data = {
            'phone_or_email': '09107412876',
            'password': '12345678'
        }
        response = self.client.post(
            reverse(self.SIGNIN_ENDPOINT), self.req_data)
        self.assertEqual(response.status_code, 201)

        # Testing user detail API
        token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(reverse(self.USER_DETAIL_ENDPOINT))
        self.assertEqual(response.status_code, 200)

        # Testing signin user phone API
        self.req_data = {
            'first_name': 'test',
            'last_name': 'user'
        }
        response = self.client.patch(
            reverse(self.USER_DETAIL_ENDPOINT), self.req_data)
        self.assertEqual(response.status_code, 200)

        # Testing changing password
        self.req_data = {
            'password': '132456789'
        }
        response = self.client.put(
            reverse(self.USER_CHANGE_PASSWORD_ENDPOINT), self.req_data)
        token = response.data.get('token')
        self.assertEqual(response.status_code, 200)

        # Testing expired token error
        response = self.client.get(reverse(self.USER_DETAIL_ENDPOINT))
        self.assertEqual(response.status_code, 401)

        # Testing user detail API
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(reverse(self.USER_DETAIL_ENDPOINT))
        self.assertEqual(response.status_code, 200)


class ResendCodeTestCase(APITestCase):
    USER_DETAIL_ENDPOINT = 'user_detail'
    VERIFY_PHONE_ENDPOINT = 'verify_phone'
    VERIFY_EMAIL_ENDPOINT = 'verify_email'
    RESEND_PHONE_ENDPOINT = 'resend_phone_code'
    RESEND_EMAIL_ENDPOINT = 'resend_email_code'

    def test_resend_code(self):
        # Setting up a user
        self.data = {
            'email': 'testcase@test.com',
            'phone': '09107412876',
            'password': '12345678',
            'email_verified': True,
            'phone_verified': True
        }
        self.user = user_model.objects.create_user(**self.data)
        token = get_tokens_for_user(self.user).get('token')

        # Testing user detail API
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(reverse(self.USER_DETAIL_ENDPOINT))
        self.assertEqual(response.status_code, 200)

        # Testing signin user phone API
        self.new_user_data = {
            'email': 'testcase2@test.com',
            'phone': '09199142331'
        }
        response = self.client.patch(
            reverse(self.USER_DETAIL_ENDPOINT), self.new_user_data)
        self.assertEqual(response.status_code, 200)

        # Testing verify user phone API
        self.req_data = {
            'phone': self.new_user_data.get('phone'),
        }
        response = self.client.post(
            reverse(self.RESEND_PHONE_ENDPOINT), self.req_data)
        print(response.data)
        self.assertEqual(response.status_code, 201)

        # Testing verify user email API
        self.req_data = {
            'email': self.new_user_data.get('email'),
        }
        response = self.client.post(
            reverse(self.RESEND_EMAIL_ENDPOINT), self.req_data)
        self.assertEqual(response.status_code, 201)

        # Testing verify user phone API
        time.sleep(0.009)
        code = cache.get(self.new_user_data.get('phone'))
        self.req_data = {
            'phone': self.new_user_data.get('phone'),
            'code': code
        }
        response = self.client.post(
            reverse(self.VERIFY_PHONE_ENDPOINT), self.req_data)
        self.assertEqual(response.data, {'phone_verified': True})

        # Testing verify user email API
        code = cache.get(self.new_user_data.get('email'))
        self.req_data = {
            'email': self.new_user_data.get('email'),
            'code': code
        }
        response = self.client.post(
            reverse(self.VERIFY_EMAIL_ENDPOINT), self.req_data)
        self.assertEqual(response.data, {'email_verified': True})
