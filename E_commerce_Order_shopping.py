import logging

# Logging Configuration
logging.basicConfig(
    filename="ECommerce.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class E_Commerce_Order_System:

    tax_percentage = 5

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.status = "pending"
        logging.info("Order created for %s with status: %s", self.product, self.status)

    def place_order(self):
        self.status = "placed"
        logging.info("Order Placed for %s", self.product)

    def cancel_order(self):
        self.status = "cancelled"
        logging.info("Order Cancelled for %s", self.product)

    def calculate_total_price(self):
        subtotal = self.price * self.quantity
        tax_amount = (subtotal * E_Commerce_Order_System.tax_percentage) / 100
        total = subtotal + tax_amount
        logging.info("Total Price for %s (with tax): %.2f", self.product, total)

    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percentage = new_tax
        logging.info("Tax percentage updated to: %d%%", new_tax)



order1 = E_Commerce_Order_System("Laptop", 50000, 1)

logging.info("Current Order Status: %s", order1.status)

order1.place_order()
order1.calculate_total_price()

print()

E_Commerce_Order_System.update_tax_percentage(12)
order1.calculate_total_price()

order1.cancel_order()
