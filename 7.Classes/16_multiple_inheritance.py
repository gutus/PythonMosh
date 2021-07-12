# Multiple Inheritance
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):  # saat class pertama nya employee maka class person akan diabaikan
    pass


manager = Manager()
manager.greet()
