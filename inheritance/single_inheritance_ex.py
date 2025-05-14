class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Programming Language: {self.programming_language}")

# Object creation and method call
dev1 = Developer("Mg Mg", 800000, "Python")
dev1.display_info()
