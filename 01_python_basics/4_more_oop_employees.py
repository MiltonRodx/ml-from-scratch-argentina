class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, name, surname, payment):
        self.name = name
        self.surname = surname
        self.payment = payment
        self.email = name.lower() + "." + surname.lower() + "@business.com"
        Employee.num_of_emps += 1

    def stats(self):
        print(f"{self.name}, {self.surname}, {self.payment:.2f}, {self.email}")

    def raise_salary(self):
        self.payment = int(self.payment* Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount): # this is going to pass the class itself as an arg
        cls.raise_amount = amount

emp_1 = Employee("Juan", "Romero", 900422)
emp_1.stats()
emp_1.raise_salary()
emp_1.stats()
print(emp_1.raise_amount)
print(Employee.raise_amount)

emp_2 = Employee("Martin", "Sanchez", 5320000)
emp_2.stats()
emp_2.raise_salary()
emp_2.stats()
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_2.__dict__)
print(Employee.num_of_emps)

print(Employee.raise_amount)
Employee.set_raise_amt(1.14)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_2.raise_amount)