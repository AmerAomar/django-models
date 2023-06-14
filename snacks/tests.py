from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack


class SnackTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.snack = Snack.objects.create(name='Test Snack', purchaser=self.user, description='Test Description')

    def test_snacks_list_page(self):
        response = self.client.get(reverse('snacksList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertContains(response, self.snack.name)
        self.assertContains(response, reverse('snackDetail', args=[self.snack.pk]))

    def test_snack_detail_page(self):
        response = self.client.get(reverse('snackDetail', args=[self.snack.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertContains(response, self.snack.name)
        self.assertContains(response, self.snack.purchaser.username)
        self.assertContains(response, self.snack.description)
        self.assertContains(response, reverse('snacksList'))
