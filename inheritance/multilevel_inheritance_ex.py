class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_person(self):
        print(f"Full Name: {self.first_name} {self.last_name}")

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id, base_salary):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.base_salary = base_salary

    def show_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Base Salary: {self.base_salary} MMK")

class Manager(Employee):
    def __init__(self, first_name, last_name, employee_id, base_salary, bonus_percent):
        super().__init__(first_name, last_name, employee_id, base_salary)
        self.bonus_percent = bonus_percent

    def calculate_total_salary(self):
        bonus = self.base_salary * (self.bonus_percent / 100)
        total = self.base_salary + bonus
        return total

    def show_manager(self):
        print(f"Bonus Percent: {self.bonus_percent}%")
        total_salary = self.calculate_total_salary()
        print(f"Total Salary with Bonus: {total_salary} MMK")

# Object creation
m = Manager("Zaw", "Min", "EMP001", 800000, 20)

# Calling methods
m.show_person()     # from Person
m.show_employee()   # from Employee
m.show_manager()    # from Manager
