import logging

logging.basicConfig(
    filename="Hostel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Hostel_Management_System:
    
    room_rent = 5000
    
    def __init__(self, student_name, months):
        self.student_name = student_name
        self.months = months
        self.allocated = "pending"
    
    def allocate_room(self):
        self.allocated = "yes"
        logging.info("Room Allocated to %s", self.student_name)
    
    def vacate_room(self):
        self.allocated = "no"
        logging.info("Room Vacated by %s", self.student_name)
    
    def calculate_monthly_fee(self):
        total = self.months * Hostel_Management_System.room_rent
        logging.info("Total Fee for %s: %d", self.student_name, total)
    
    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent = new_rent


room1 = Hostel_Management_System("Padmini", 6)

room1.allocate_room()
room1.calculate_monthly_fee()

print()

Hostel_Management_System.update_room_rent(6000)
room1.calculate_monthly_fee()

room1.vacate_room()
