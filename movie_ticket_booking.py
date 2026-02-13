import logging

logging.basicConfig(
    filename="Movie.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Movie_Ticket_Booking:
    
    ticket_price = 200
    
    def __init__(self, movie_name, seats):
        self.movie_name = movie_name
        self.seats = seats
        self.is_booked = False
    
    def book_seat(self):
        self.is_booked = True
        logging.info("Seats booked for movie: %s", self.movie_name)
    
    def cancel_booking(self):
        self.is_booked = False
        logging.info("Booking cancelled for movie: %s", self.movie_name)
    
    def calculate_ticket_price(self):
        total = self.seats * Movie_Ticket_Booking.ticket_price
        logging.info("Total Ticket Price for %s: %d", self.movie_name, total)
        
    @classmethod
    def update_ticket_price(cls, new_ticket_price):
        cls.ticket_price = new_ticket_price


movie1 = Movie_Ticket_Booking("Husharu", 3)

movie1.book_seat()
movie1.calculate_ticket_price()
Movie_Ticket_Booking.update_ticket_price(300)
movie1.calculate_ticket_price()
movie1.cancel_booking()
