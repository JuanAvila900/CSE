class Person(object):
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def work(self):
        print("%s goes to work" % self.name)

class Employee(Person):
    def __init__(self, name, age, size, work):
        super(Employee, self).__init__(name, age, size)
        self.work = work

    def work(self):
        print("The employee works on fifty pieces of paper, full of contracts")


class Programmer(Person
                 ):
    def __init__(self, name, age, item):
        super(Programmer, self).__init__(name, age, item)

    def program(self):
        print("You programmed the whole computer system")
