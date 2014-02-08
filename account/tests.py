from .models import Account
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class UserTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register(self):
        response = self.client.post(reverse('registration_register'),
                                    {
                                        # 'username': 'foo',
                                        'password1': 'bar',
                                        'password2': 'bar',
                                        'email': 'bar@example.com',
                                    }
                                    )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Account.objects.filter(is_active=True).count(), 1)
