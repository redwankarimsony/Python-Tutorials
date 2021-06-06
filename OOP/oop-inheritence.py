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

class Developer(Employee):
    def __init__(self, first, last, pay, language: str = 'C++') -> None:
        super().__init__(first, last, pay)
        self.language = language

    def __str__(self) -> str:
        return f"{self.first}  {self.last} {self.pay} {self.language}"

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees =[]
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print(f"{emp} is already present in the list")
    
    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print(f"{emp} is not found the the subordinate list")

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp)
            


dev1  = Developer('Sabbira', "Easmin", 50000, 'Python')
dev2  = Developer('Redwan', "Karim", 3500, "JavaScript")

mgr1 = Manager('Manager', 'One', 50000, employees=[dev1])

mgr1.print_employees()
print("After adding")
mgr1.add_employee(dev2)

mgr1.print_employees()
print('After removing')
mgr1.remove_employees(dev1)
mgr1.print_employees()




