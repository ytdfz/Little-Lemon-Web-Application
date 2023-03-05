from django.test import TestCase
from restaurant.models import MenuItem

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='IceCream', price=80)
        self.assertEqual(str(item), 'IceCream : 80')