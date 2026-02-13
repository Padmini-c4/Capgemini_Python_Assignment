import logging

logging.basicConfig(
    filename="Employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Employee_Payroll_system:
    
    hra_percentage = 20
    
    def __init__(self, name, basic_salary, leaves=0):
        self.name = name
        self.basic_salary = basic_salary
        self.leaves = leaves
    
    def calculate_salary(self):
        hra = self.basic_salary * Employee_Payroll_system.hra_percentage / 100
        total = self.basic_salary + hra
        return total
    
    def apply_leave_deduction(self):
        deduction = self.leaves * 500
        return deduction
    
    def display_payslip(self):
        gross = self.calculate_salary()
        deduction = self.apply_leave_deduction()
        net = gross - deduction
        logging.info("Employee: %s", self.name)
        logging.info("Net Salary: %.2f", net)
    
    @classmethod
    def update_hra_percentage(cls, new_hra):
        cls.hra_percentage = new_hra


emp1 = Employee_Payroll_system("Padmini", 30000, 2)

emp1.display_payslip()

print()

Employee_Payroll_system.update_hra_percentage(30)
emp1.display_payslip()
