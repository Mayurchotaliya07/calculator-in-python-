class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        if self.b == 0:
            raise ValueError("you cannot divide a number by 0")
        
        return self.a / self.b
    
def input_value():
    
    print("Welcome to calculator app")
    
    a = int(input("Enter your first: "))
    b = int(input("Enter your second number: "))

    calculations = Calculator(a,b)

    print("1. Addition")
    print("2. subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        sign = int(input("What you wanted to do (1 to 4): "))
        if sign == 1:
            print(f"{a} + {b} = {calculations.add()}")
            break
        elif sign == 2:
            print(f"{a} - {b} = {calculations.sub()}")
            break
        elif sign == 3:
            print(f"{a} * {b} = {calculations.mul()}")
            break
        elif sign == 4:
            print(f"{a} / {b} = {calculations.div()}")
            break
        else:
            print("Enter a number from (1 to 4)")
    

input_value()