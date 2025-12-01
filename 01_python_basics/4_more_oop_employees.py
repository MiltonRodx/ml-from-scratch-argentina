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

# inheritance
class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, payment, prog_lang):
        super().__init__(first, last, payment)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, name, surname, payment, employees=None):
        super().__init__(name, surname, payment)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for employee in self.employees:
            print(self.__dict__(employee))



# testing & print
# emp_1 = Employee("Juan", "Romero", 900422)
# emp_1.stats()
# emp_1.raise_salary()
#emp_1.stats()
#print(Employee.raise_amount)

#emp_2 = Employee("Martin", "Sanchez", 5320000)
#emp_2.stats()
#emp_2.raise_salary()
#emp_2.stats()
#print(emp_2.raise_amount)
#print(Employee.raise_amount)

#print(emp_2.__dict__)
#print(Employee.num_of_emps)

#print(Employee.raise_amount)
#Employee.set_raise_amt(1.14)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
#print(emp_2.raise_amount)

man = Manager("Julio", "Acosta", 1999999, None)
man.print_emps()


dev_1 = Developer("Corey", "Schafer", 45000000, "Python")
dev_2 = Developer("Sandro", "Sanchez", 653000, "Java")
dev_3 = Developer("Hola", "Mundo", 333333333333333333333, "Javascript")
dev_1.stats()
dev_2.stats()
dev_3.stats()
print(dev_1.__dict__)

print("\n")
print(dev_1.payment)
dev_1.raise_salary()
print(dev_1.payment)

man.print_emps()