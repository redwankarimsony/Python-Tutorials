import datetime

class Employee:
    raise_amount = 1.04
    num_of_employee = 0
    def __init__(self, first, last, pay) -> None:
        self.first =first.replace(' ', '_')
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + "@company.com"
        Employee.num_of_employee += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    def __str__(self) -> str:
        return f"{self.first}  {self.last} {self.pay} "

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount   

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        return  day.weekday()==5 or day.weekday() ==6



emp1  = Employee('Sabbira', "Easmin", 50000)
emp2  = Employee('Redwan', "Karim", 3500)

emp_str_1 = "John-Doe-7000"
emp_str_2 = "Steve-Smith-10000"
emp_str_3 = "John-Doe-9000"

# first, last , pay = emp_str_1.split('-')


new_emp_1 = Employee.from_string(emp_str_2)
print(new_emp_1)

my_date = datetime.date(2021, 5, 6)
print(my_date)

print(Employee.is_workday(my_date))
