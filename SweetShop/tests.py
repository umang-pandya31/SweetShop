from django.test import TestCase
from django.urls import reverse
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

    def test_filter_by_price_range(self):
        models.Sweet.objects.create(name="ChocoBar", category="chocolate", price=100.00, quantity=10)
        response = self.client.get(reverse("index"), {'min_price': 20, 'max_price': 120})
        self.assertContains(response, "ChocoBar")
        self.assertNotContains(response, "rasogulla")

    def test_sort_by_price_desc(self):
        models.Sweet.objects.create(name="ChocoBar", category="chocolate", price=100.00, quantity=10)
        models.Sweet.objects.create(name="Coco", category="chocolate", price=10.00, quantity=10)
        response = self.client.get(reverse('index'), {'sort': 'price_desc'})
        sweets = list(response.context['sweets'])
        self.assertEqual(sweets[0].name, "ChocoBar")  # expensive
        self.assertEqual(sweets[-1].name, "Coco")   # Cheapest

    def test_sort_by_name_asc(self):
        models.Sweet.objects.create(name="ChocoBar", category="chocolate", price=100.00, quantity=10)
        models.Sweet.objects.create(name="Coco", category="chocolate", price=10.00, quantity=10)
        response = self.client.get(reverse('index'), {'sort': 'name_asc'})
        sweets = list(response.context['sweets'])
        names = [s.name for s in sweets]
        self.assertEqual(names, sorted(names))

    def test_sort_by_quantity_desc(self):
        models.Sweet.objects.create(name="ChocoBar", category="chocolate", price=100.00, quantity=10)
        models.Sweet.objects.create(name="Coco", category="chocolate", price=10.00, quantity=5)
        response = self.client.get(reverse('index'), {'sort': 'quantity_desc'})
        sweets = list(response.context['sweets'])
        quantities = [s.quantity for s in sweets]
        self.assertEqual(quantities, sorted(quantities, reverse=True))

    def test_purchase(self):
        sweet=models.Sweet.objects.create(name="ChocoBar", category="chocolate", price=100.00, quantity=10)
        sweet.purchase(5)
        self.assertEqual(sweet.quantity,5)
        # sweet.purchase(6)
        # self.assertEqual(sweet.quantity,6)

    def test_restock(self):
        sweet=models.Sweet.objects.create(name="ChocoBar", category="chocolate", price=100.00, quantity=10)
        sweet.restock(5)
        self.assertEqual(sweet.quantity,15)