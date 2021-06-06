class Employee:
    def __init__(self, first, last, pay) -> None:
        self.first =first.replace(' ', '_')
        self.last = last
        self.email = self.first + '.' + self.last + "@company.com"
    
    def fullname(self):
        return f"{self.first} {self.last}"



emp1 = Employee("Md. Redwan Karim", "Sony", 50000)
emp2 = Employee("Sabbira", "Easmin", 100000)

print(emp1.fullname())

print(Employee.fullname(emp2))




