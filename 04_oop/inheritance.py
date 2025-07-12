# A class(child or sub class) inherits properties and methods from another class(parent or super class)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working as a regular employee!")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def conducting_meeting(self):
        print(f"{self.name} is conducting meeting with {self.team_size} team members")

    def work(self):
        print(f"{self.name} is managing a team of {self.team_size} employees")

emp = Employee("Pranay",2000000)
emp1 = Manager("Pranay",2000000,5) 
emp1.work()
emp1.conducting_meeting()
