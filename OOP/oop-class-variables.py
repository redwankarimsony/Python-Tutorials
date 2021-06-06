
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


emp1  = Employee('Sabbira', "Easmin", 50000)
emp2  = Employee('Redwan', "Karim", 3500)

print(emp1.pay)
print(emp2.pay)

emp1.apply_raise()
print(emp1.pay)

print('--------Summary---------')
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

print('________________LOCAL__________________')
emp1.raise_amount = 2.00
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

print('________________GLOBAL__________________')
Employee.raise_amount = 2.00
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)
