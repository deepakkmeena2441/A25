class calculator:
    def __init__(self):
        self.number_1=None
        self.number_2=None
    def set_values(self,number1,number2):
        self.number_1=number1
        self.number_2=number2
    def addition(self):
        return (self.number_1 + self.number_2)
    def subtraction(self):
        return (self.number_1 - self.number_2)
s=calculator()
s.set_values(3,4)
print(s.addition())
print(s.subtraction())
