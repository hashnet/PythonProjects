from abc import ABCMeta, abstractmethod


class Person:                           # parent class
    def __init__(self, name):
        self._name = name


class Study(metaclass=ABCMeta):         # interface
    @abstractmethod
    def study(self):
        """Performs study"""


class Student(Person, Study):           # class Student extends Person implements Study
    def __init__(self, name, sid):
        super().__init__(name)
        self._sid = sid

    def study(self):
        print('{} having id {} is learning {}'.format(self._name, self._sid, 'python'))


if __name__ == '__main__':              # void main()
    alice = Student('Alice', 1)
    bob = Student('Bob', 2)

    alice.study()
    bob.study()

