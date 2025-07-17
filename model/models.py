from django.db import models

# This is a database model for sweet shop Management 
class Sweet(models.Model):
    #Here i do not take id because in django unique id is automatic generated.
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=False)
    quantity = models.PositiveIntegerField(null=False)


    #this function help us to decrease the amount of stock and we also achive ENCAPSULATION.
    def purchase(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock!")
        self.quantity -= amount
        self.save()

    #this function help us to increase the amount of stock and we also achive ENCAPSULATION.
    def restock(self, amount):
        self.quantity += amount
        self.save()