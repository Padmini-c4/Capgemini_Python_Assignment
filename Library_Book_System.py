import logging

# Logging Configuration
logging.basicConfig(
    filename="Library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class LibraryBook:

    fine_per_day = 10
    

    def __init__(self, title, author, days_late=0):
        self.title = title
        self.author = author
        self.days_late = days_late
        self.is_issued = False

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            logging.info("Book Issued: %s", self.title)
        else:
            logging.warning("Book '%s' is already issued.", self.title)

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            logging.info("Book Returned: %s", self.title)
        else:
            logging.warning("Book '%s' was not issued.", self.title)

    def calculate_fine(self):
        fine = self.days_late * LibraryBook.fine_per_day
        logging.info("Fine for '%s' is: %d", self.title, fine)

    @classmethod
    def update_fine_per_day(cls, new_fine):
        cls.fine_per_day = new_fine
        logging.info("Fine per day updated to: %d", new_fine)


# Object Creation
book1 = LibraryBook("Python Basics", "Guido", 3)

book1.issue_book()
book1.calculate_fine()

print()

LibraryBook.update_fine_per_day(20)

book1.calculate_fine()

print()

book1.return_book()
