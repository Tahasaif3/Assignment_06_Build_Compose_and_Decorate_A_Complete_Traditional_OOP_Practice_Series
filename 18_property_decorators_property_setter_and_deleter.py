#18. Property Decorators: @property, @setter, and @deleter
"""
Assignment:
Create a class Product with a private attribute _price. Use @property to get the 
price, @price.setter to update it, and @price.deleter to delete it.
"""

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Get the price."""
        return self._price
    
    @price.setter
    def price(self, new_price):
        """Set the price."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    @price.deleter
    def price(self):
        """Delete the price."""
        del self._price
        print("Price deleted.")

# Example usage
product = Product(100)
print(product.price) 
product.price = 150
print(product.price)
del product.price
