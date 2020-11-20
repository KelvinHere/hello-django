from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_done_field_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)  # Check done defaults to false

