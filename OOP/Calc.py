"""
Calculator Example
"""

class Calc:
    def add(self, *args):
        return sum(args)
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, *args):
        res = 1
        for num in args:
            res *= num
        return res
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

def test_operations():

    calc = Calc()
    assert calc.add(5, 3) == 8
    assert calc.subtract(5, 3) == 2
    assert calc.multiply(5, 3) == 15
    assert calc.divide(6, 3) == 2