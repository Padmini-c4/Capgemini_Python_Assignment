import logging

# Logging Configuration
logging.basicConfig(
    filename="OnlineExam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Online_Exam_System:

    pass_marks = 35

    def __init__(self, student_name, total_marks, obtained_marks=0):
        self.student_name = student_name
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks
        self.started = False
        self.submitted = False

    def start_exam(self):
        if not self.started and not self.submitted:
            self.started = True
            logging.info("Exam started for %s", self.student_name)
        else:
            logging.warning("Cannot start exam for %s", self.student_name)

    def submit_exam(self):
        if self.started and not self.submitted:
            self.submitted = True
            self.started = False
            logging.info("Exam submitted by %s", self.student_name)
        else:
            logging.warning("Cannot submit exam for %s", self.student_name)

    def calculate_score(self):
        if self.total_marks == 0:
            logging.error("Total marks cannot be zero for %s", self.student_name)
            return

        percentage = (self.obtained_marks / self.total_marks) * 100
        logging.info("Score of %s is: %.2f%%", self.student_name, percentage)

        if percentage >= Online_Exam_System.pass_marks:
            logging.info("Result of %s: PASS", self.student_name)
        else:
            logging.info("Result of %s: FAIL", self.student_name)

    @classmethod
    def update_pass_marks(cls, new_marks):
        cls.pass_marks = new_marks
        logging.info("Pass marks updated to: %d", new_marks)



exam1 = Online_Exam_System("Padmini", 100, 75)

exam1.start_exam()
exam1.calculate_score()
exam1.submit_exam()

print()

Online_Exam_System.update_pass_marks(50)
exam1.calculate_score()
