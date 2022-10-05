class phone:
    def uses(self):
        print("Calling ")
        print("Sms")
class calculator:
    def __init__(self):
        self.number1=None
        self.number2=None
    def set_Values(self,num1,num2):
        self.number1=num1
        self.number2=num2
    def multiplication(self):
        return(self.number1 * self.number2)
    def division(self):
        return (self.number1//self.number2)
class calculator2(calculator):
    pass
class smartphone(phone,calculator2):
    pass
samsung=smartphone()
samsung.uses()

