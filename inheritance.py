class Person:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname

    def printname(self):
        print(self.first, self.last)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        print(self.first, self.last, self.year)


x = Student("Mike", "Olsen", 2019)
x.welcome()
