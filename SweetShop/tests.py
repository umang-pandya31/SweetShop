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