from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Item, Category, Tag

class CategoryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="Electronics")

    def test_create_category(self):
        """
        Ensure we can create a new category.
        """
        url = reverse('category-list') # Adjust based on your URL naming
        data = {'name': 'Books'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(id=2).name, 'Books')

    def test_get_categories(self):
        """
        Ensure we can retrieve a list of categories.
        """
        url = reverse('category-list') # Adjust based on your URL naming
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # Adjust based on initial data


class ItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(name="Laptop", sku="LAP123", category=self.category, stock_status="In Stock", available_stock=10)

    def test_create_item(self):
        """
        Ensure we can create a new item.
        """
        url = reverse('item-list') # Adjust based on your URL naming
        data = {
            'name': 'Smartphone',
            'sku': 'SMP123',
            'category': self.category.id,
            'stock_status': 'In Stock',
            'available_stock': 15
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(Item.objects.get(id=2).name, 'Smartphone')

    def test_get_item(self):
        """
        Ensure we can retrieve an item.
        """
        url = reverse('item-detail', args=[self.item.id]) # Adjust based on your URL naming
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Laptop')
