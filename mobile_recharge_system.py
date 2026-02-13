import logging

logging.basicConfig(
    filename="MobileRecharge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Mobile_Recharge_System:
    
    plans = {"Basic": 199, "Premium": 399}
    
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance
        self.validity_days = 0

    def do_recharge(self, amount):
        self.balance += amount
        if amount >= 199:
            self.validity_days += 30
        logging.info("Recharge Successful for %s", self.user)
    
    def check_validity(self):
        logging.info("Valid days for %s: %d", self.user, self.validity_days)
    
    def show_balance(self):
        logging.info("Balance for %s: %d", self.user, self.balance)
    
    @classmethod
    def update_recharge_plan(cls, plan_name, price):
        cls.plans[plan_name] = price
        logging.info("Updated Plans: %s", cls.plans)


user1 = Mobile_Recharge_System("Padmini", 100)

user1.show_balance()
user1.do_recharge(299)
user1.check_validity()

print()

Mobile_Recharge_System.update_recharge_plan("Gold", 599)
logging.info("Updated Plans: %s", Mobile_Recharge_System.plans)
