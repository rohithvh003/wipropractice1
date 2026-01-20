from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass
