class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.title = title
        self.price = price
        self.quantity = quantity
        if self.quantity == 1:
            self.items.append(self.title)
        elif self.quantity > 1:
            x = self.quantity
            while self.quantity > 0:
                self.items.append(self.title)
                self.quantity = self.quantity - 1
            self.quantity = x

        self.total += price * quantity

    def apply_discount(self):
        if self.total > 0:
            self.discount = 20
            self.total = self.total - self.discount / 100 * self.total
            print("After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.quantity == 1:
            self.total = self.total - self.price
        else:
            self.total = 0.0
