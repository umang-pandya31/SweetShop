from django.test import TestCase
from model import models

class SweetModelTest(TestCase):
    #For add_sweet, test case is run successfully. 
    def test_add_sweet(self):
        sweet = models.Sweet.objects.create(
            name="Rasgulla",
            category="Bangoli",
            price=320.00,
            quantity=50
        )
        self.assertEqual(sweet.name, "Rasgulla") #Check value
        self.assertEqual(sweet.quantity, 50) #Check value

    def test_delete_sweet(self):
        sweet = models.Sweet.objects.create(  #Create dummy data
            name="Lollipop",
            category="candy",
            price=2.00,
            quantity=30
        )
        sweet_id = sweet.id
        sweet.delete()
        self.assertFalse(models.Sweet.objects.filter(id=sweet_id).exists())

    def test_update_sweet(self):
        sweet = models.Sweet.objects.create( #Create dummy data
            name="kitkat",
            category="chocolate",
            price=15.00,
            quantity=20
        )
        sweet.price = 18.00
        sweet.quantity = 25
        sweet.save()
        updated = models.Sweet.objects.get(id=sweet.id)
        self.assertEqual(updated.price, 18.00)
        self.assertEqual(updated.quantity, 25)

    def test_search_sweet(self):
        models.Sweet.objects.create(name="kitkat", category="chocolate", price=15.00, quantity=20)
        models.Sweet.objects.create(name="Kit Roll", category="chocolate", price=18.00, quantity=15)

        sweets = models.Sweet.objects.filter(category="chocolate")

        for sweet in sweets:  #we iterat loop because match sweets is more than one
            self.assertEqual(sweet.category, "chocolate")