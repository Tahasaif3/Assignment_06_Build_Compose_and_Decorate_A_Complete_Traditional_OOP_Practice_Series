#4. Class Variables and Class Methods

"""
Assignment:
Create a class Bank with a class variable bank_name.
Add a class method change_bank_name(cls, name) that
allows changing the bank name. Show that it affects
all instances of the class.
"""

class Bank:
    bank_name = "HBL Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to: {cls.bank_name}")

    def show_bank_name(self):
        print(f"Bank name is: {self.bank_name}")

bank1 = Bank()
bank1.show_bank_name()
Bank.change_bank_name("UBL Bank")
bank1.show_bank_name()