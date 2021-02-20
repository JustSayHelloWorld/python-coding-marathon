"""Define a class Employee. In the class Employee implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash.

Examples:
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp1.firstname ➞ "Mary"
emp1.salary ➞ 60000
emp2.firstname ➞ "John""""


class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        list = string.split("-")

        return cls(list[0], list[1], list[2])