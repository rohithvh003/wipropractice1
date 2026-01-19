# 2. Create another class AdvancedCalculator that overrides a method from Calculator
class Calculator:
    def calculate(self, a, b):
        print(a + b)


class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print(a * b)


ac = AdvancedCalculator()
ac.calculate(4, 5)
