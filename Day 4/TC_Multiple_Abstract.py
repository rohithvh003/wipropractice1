from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class SBI(Bank):
    def interest(self):
        print("interest is 10%")

    def loan(self):
        print("loan is available")

s1 = SBI()
s1.loan()
s1.interest()




