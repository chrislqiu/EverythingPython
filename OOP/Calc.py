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
