from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='testpass',
            email='test@example.com',
            cin='1234567890',
            gender='male',
            phone_number='123456789'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.cin, '1234567890')
        self.assertEqual(user.gender, 'male')
        self.assertEqual(user.phone_number, '123456789')
        self.assertTrue(user.check_password('testpass'))

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='adminuser',
            password='adminpass',
            email='admin@example.com',
            cin='9876543210',
            gender='female',
            phone_number='987654321'
        )
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)
