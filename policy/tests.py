from django.test import TestCase
from rest_framework.test import APIClient

from .models import PolicyAcknowledgment


class PolicyAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_current_policy(self):
        response = self.client.get('/api/current-policy/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('version', response.data)
        self.assertIn('content', response.data)
        self.assertIn('effective_date', response.data)

    def test_acknowledge_success(self):
        response = self.client.post(
            '/api/acknowledge/',
            {'user_name': 'hiro', 'policy_version': '1.0'},
            format='json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn('acknowledged_at', response.data)
        self.assertEqual(PolicyAcknowledgment.objects.count(), 1)

    def test_acknowledge_missing_fields(self):
        response = self.client.post('/api/acknowledge/', {}, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(PolicyAcknowledgment.objects.count(), 0)

    def test_acknowledge_wrong_version(self):
        response = self.client.post(
            '/api/acknowledge/',
            {'user_name': 'hiro', 'policy_version': '9.9'},
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(PolicyAcknowledgment.objects.count(), 0)
