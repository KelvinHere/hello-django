from django.db import models


# Create your models here.
# models.Model allows this class to do everything the
# django model class can do (class inheritance)
class Item(models.Model):
    # These variabales create fields in the Item database (this class)
    # built in django field, characters
    name = models.CharField(max_length=50, null=False, blank=False)
    # boolean field
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        # Return the item classes name attribute in this
        # case the name in the form.
        # Override the __str__ method to change how the items are
        # displayed, show item names instead of object1 or object2
        return self.name
