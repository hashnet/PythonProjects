class Person:
    def __init__(self, name):
        self._name = name

    def sayHello(self):
        print('Hi my name is {}.'.format(self._name))


najat = Person('Najat')
namir = Person('Namir')

najat.sayHello()
Person.sayHello(namir)      # Calling non-static method in static mannerxs
