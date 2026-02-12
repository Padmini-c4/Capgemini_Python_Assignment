import logging

logging.basicConfig(
    filename="Hospital.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Patient:

    hospital_name = "Kims Hospital"
    consultation_fee = 500

    def __init__(self, name, age, disease, days_admitted):
        self.name = name
        self.age = age
        self.disease = disease
        self.days_admitted = days_admitted
        self.is_admitted = False

    def admit_patient(self):
        if not self.is_admitted:
            self.is_admitted = True
            logging.info(" %s has been admitted.",self.name)
        else:
            logging.warning("%s is already admitted.",self.name)

    def discharge_patient(self):
        if self.is_admitted:
            self.is_admitted = False
            logging.info("%s has been discharged.",self.name)
        else:
            logging.warning("%s is not admitted.",self.name)

    def calculate_bill(self):
        if self.is_admitted:
            room_charge_per_day = 2000
            total = (self.days_admitted * room_charge_per_day) + Patient.consultation_fee
            logging.info(f"Total Bill for {self.name} is: {total}")
            print(f"Total Bill for {self.name} is: {total}")
        else:
            logging.warning("Patient not admitted.")
            print("Patient not admitted.")

    @classmethod
    def update_consultation_fee(cls, new_fee):
        cls.consultation_fee = new_fee
        logging.info(f"Consultation Fee Updated to: {new_fee}")
        print("Consultation Fee Updated to:", new_fee)


# Object Creation
p1 = Patient("Padmini", 22, "Fever", 3)

p1.admit_patient()
p1.calculate_bill()

print()

Patient.update_consultation_fee(800)

p1.calculate_bill()

print()

p1.discharge_patient()
