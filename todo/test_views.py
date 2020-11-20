from django.test import TestCase
from .models import Item   # Import the Item class for the edit test

class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Is the response error code correct
        self.assertTemplateUsed(response, 'todo/todo_list.html')  # Check that the template used in response is the todo_list.html template

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item') # Add a test item
        response = self.client.get(f'/edit/{item.id}')  # Pass test item to client.get
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})  # Add an item
        self.assertRedirects(response, '/')  # Check that after item is added you are redirected to /

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item') # Add a test item
        response = self.client.get(f'/delete/{item.id}')  # Request item is deleted
        self.assertRedirects(response, '/')  # Check that after item is added you are redirected to /
        existing_items = Item.objects.filter(id=item.id)  # Search DB for items with ID of the deleted item
        self.assertEqual(len(existing_items), 0)  # Make sure the returned existing items list is empty

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True) # Add a test item
        response = self.client.get(f'/toggle/{item.id}')  # Request item toggle
        self.assertRedirects(response, '/')  # Check that after item is toggled you are redirected to /
        updated_item = Item.objects.get(id=item.id)  # Get the toggled item
        self.assertFalse(updated_item.done)  # Updated item should now be false

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True) # Add a test item
        response = self.client.post(f'/edit/{item.id}', {'name': 'new updated name'})  # Post new updated name to edit item
        self.assertRedirects(response, '/')  # Check that after item is edited you are redirected to /
        updated_item = Item.objects.get(id=item.id)  # Get the toggled item
        self.assertEqual(updated_item.name, 'new updated name')
        
