import logging

logging.basicConfig(
    filename="Railway.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Railway_Ticket_Booking:
    
    base_fare = 100
    
    def __init__(self, passenger_name, distance):
        self.passenger_name = passenger_name
        self.distance = distance
        self.status = "Pending"
    
    def book_ticket(self):
        self.status = "Booked"
        logging.info("Ticket booked for %s", self.passenger_name)

    def cancel_ticket(self):
        self.status = "Cancelled"
        logging.info("Ticket cancelled for %s", self.passenger_name)

    def calculate_fare(self):
        fare = self.distance * Railway_Ticket_Booking.base_fare
        logging.info("Total Fare for %s: %d", self.passenger_name, fare)
    
    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare


ticket1 = Railway_Ticket_Booking("Padmini", 10)

ticket1.book_ticket()
ticket1.calculate_fare()

print()

Railway_Ticket_Booking.update_base_fare(150)
ticket1.calculate_fare()

ticket1.cancel_ticket()
